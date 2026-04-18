from brasa.core.nodes.primitive_values import IntegerValue,NullValue
from brasa.core.utils.operators.map import BINARY_OPS_MAP

class VariablesMixin:
  def visit_Identifier(self,node):
    entity_id=self.current_scope.lookup(node.name)

    return self.world.get_value(entity_id)

  def visit_VariableDeclarationStatement(self,node):
    value=self.visit(node.expr) if node.expr is not None else NullValue

    entity_id=self.world.create(
      type=node.type,
      value=value,
      is_const=node.is_const
    )

    self.current_scope.declare(
      name=node.id.name,
      entity_id=entity_id
    )

  def visit_AssignmentStatement(self,node):
    value=self.visit(node.expr)
    node.lvalue.set(self,value)

  def visit_CompoundAssignmentStatement(self,node):
    current=node.lvalue.get(self)
    value=self.visit(node.expr)

    func=BINARY_OPS_MAP[node.op]
    result=func(current,value)

    node.lvalue.set(self,result)

  def visit_PostfixStatement(self,node):
    current=node.lvalue.get(self)

    func=BINARY_OPS_MAP[node.op]
    new_value=func(current,IntegerValue(1))

    node.lvalue.set(self,new_value)
