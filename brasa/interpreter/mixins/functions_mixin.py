from brasa.core.runtime.scope import Scope

from brasa.core.nodes.functions import FunctionValue,BuiltinFunction
from brasa.core.types.signals import ReturnSignal

class FunctionsMixin:
  def visit_FunctionDeclarationStatement(self,node):
    func=FunctionValue(
      params=node.params,
      body=node.body,
      return_type=node.return_type,
      closure_scope=self.current_scope
    )

    entity_id=self.world.create(
      type=None,
      value=func,
      is_const=True
    )

    self.current_scope.declare(
      name=node.name.name,
      entity_id=entity_id
    )

  def visit_LambdaExpression(self,node):
    return FunctionValue(
      params=node.parameters,
      body=node.body,
      return_type=node.return_type,
      closure_scope=self.current_scope,
    )
  
  def visit_CallExpression(self,node):
    func=self.visit(node.callee)
    args=[self.visit(arg) for arg in node.args]

    if isinstance(func,BuiltinFunction):
      return func.func(*args)

    new_scope=Scope(parent=func.closure_scope)

    for param, arg in zip(
      func.params,
      args
    ):
      entity_id=self.world.create(type=param[0], value=arg)
      new_scope.declare(
        name=param[1].name,
        entity_id=entity_id
      )

    old_scope=self.current_scope
    self.current_scope=new_scope

    try:
      self.visit(func.body)
      result=None
    except ReturnSignal as r:
      result=r.value

    self.current_scope=old_scope

    return result

  def visit_ReturnStatement(self, node):
    value=None

    if node.expr:
      value=self.visit(node.expr)

    raise ReturnSignal(value)
