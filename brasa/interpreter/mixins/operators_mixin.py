from brasa.core.utils.operators.map import BINARY_OPS_MAP,UNARY_OPS_MAP

class OperatorsMixin:
  def visit_BinaryOperation(self,node):
    left=self.visit(node.left)
    right=self.visit(node.right)

    func=BINARY_OPS_MAP[node.op]
    return func(left,right)

  def visit_UnaryOperation(self,node):
    operand=self.visit(node.expr)
    func=UNARY_OPS_MAP[node.op]
    return func(operand)
