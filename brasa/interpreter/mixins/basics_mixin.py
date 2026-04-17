from brasa.core.runtime.scope import Scope

class BasicsMixin:
  def visit_Program(self,node):
    for statement in node.statements:
      self.visit(statement)

  def visit_Block(self,node):
    old_scope=self.current_scope
    self.current_scope=Scope(parent=old_scope)

    for stmt in node.statements:
      self.visit(stmt)

    self.current_scope=old_scope

  def visit_PrintStatement(self,node):
    value=self.visit(node.expr)

    if value is None:
      print('nulo')
    elif value is True:
      print('verdadeiro')
    elif value is False:
      print('falso')
    else:
      print(value)
