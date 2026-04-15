from brasa.core.types.signals import BreakSignal,ContinueSignal

class FlowMixin:
  def visit_IfStatement(self,node):
    condition=self.visit(node.condition)

    if condition: return self.visit(node.then_block)
    if node.else_branch: return self.visit(node.else_branch)

  def visit_WhileStatement(self,node):
    while self.visit(node.condition):
      try: self.visit(node.body)
      except ContinueSignal: continue
      except BreakSignal: break

  def visit_BreakStatement(self,_): raise BreakSignal()
  def visit_ContinueStatement(self,_): raise ContinueSignal()
