from brasa.core.runtime.scope import Scope

class BasicsMixin:
  def visit_Program(self,node):
    for statement in node.statements: self.visit(statement)

  def visit_Block(self,node):
    old_scope=self.current_scope
    self.current_scope=Scope(parent=old_scope)

    for statement in node.statements: self.visit(statement)

    self.current_scope=old_scope
