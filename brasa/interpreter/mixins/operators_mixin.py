from brasa.core.types.operators import BinaryOperationEnum,UnaryOperationEnum

class OperatorsMixin:
  def visit_BinaryOperation(self,node):
    op=node.op

    if op==BinaryOperationEnum.AND:
      left=self.visit(node.left)

      if not left:
        return False

      right=self.visit(node.right)
      return bool(right)

    if node.op==BinaryOperationEnum.OR:
      left=self.visit(node.left)

      if left:
        return True

      right=self.visit(node.right)
      return bool(right)

    left=self.visit(node.left)
    right=self.visit(node.right)

    if op==BinaryOperationEnum.ADDITION:
      return left+right
    if op==BinaryOperationEnum.SUBTRACTION:
      return left-right
    if op==BinaryOperationEnum.MULTIPLICATION:
      return left*right
    if op==BinaryOperationEnum.DIVISION:
      return left/right

    if op==BinaryOperationEnum.GREATER_THAN:
      return left>right
    if op==BinaryOperationEnum.LESS_THAN:
      return left<right
    if op==BinaryOperationEnum.GREATER_THAN_OR_EQUAL_TO:
      return left>=right
    if op==BinaryOperationEnum.LESS_THAN_OR_EQUAL_TO:
      return left<=right
    if op==BinaryOperationEnum.EQUAL:
      return left==right
    if op==BinaryOperationEnum.NOT_EQUAL:
      return left!=right

    raise Exception(f'Unknown binary operator: {op}')

  def visit_UnaryOperation(self,node):
    value=self.visit(node.expr)

    if node.op==UnaryOperationEnum.NEGATIVE:
      return -value

    if node.op==UnaryOperationEnum.NOT:
      return not value

    raise Exception(f'Unknown unary operator: {node.op}')
