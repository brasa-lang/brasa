from brasa.core.types.operators import BinaryOperationEnum,UnaryOperationEnum

from brasa.core.utils.operators.binary import add,sub,mul,div,remainder,greater_than,less_than,less_than_or_equal_to,greater_than_or_equal_to,equal,not_equal,and_,or_
from brasa.core.utils.operators.unary import not_,negative

class OperatorsMixin:
  def visit_BinaryOperation(self,node):
    op = node.op

    left = self.visit(node.left)
    right = self.visit(node.right)

    # -------- ARITHMETIC --------

    if op == BinaryOperationEnum.ADDITION:
      return add(left,right)

    if op == BinaryOperationEnum.SUBTRACTION:
      return sub(left,right)

    if op == BinaryOperationEnum.MULTIPLICATION:
      return mul(left,right)

    if op == BinaryOperationEnum.DIVISION:
      return div(left,right)

    if op == BinaryOperationEnum.REMAINDER:
      return remainder(left,right)

    # -------- COMPARISON --------

    if op == BinaryOperationEnum.GREATER_THAN:
      return greater_than(left,right)

    if op == BinaryOperationEnum.LESS_THAN:
      return less_than(left,right)

    if op == BinaryOperationEnum.GREATER_THAN_OR_EQUAL_TO:
      return greater_than_or_equal_to(left,right)

    if op == BinaryOperationEnum.LESS_THAN_OR_EQUAL_TO:
      return less_than_or_equal_to(left,right)

    if op == BinaryOperationEnum.EQUAL:
      return equal(left,right)

    if op == BinaryOperationEnum.NOT_EQUAL:
      return not_equal(left,right)

    # -------- LOGIC --------

    if op == BinaryOperationEnum.AND:
      return and_(left,right)

    if op == BinaryOperationEnum.OR:
      return or_(left,right)

    raise Exception(f'Unknown binary operator: {op}')

  def visit_UnaryOperation(self,node):
    value = self.visit(node.expr)

    if node.op == UnaryOperationEnum.NEGATIVE:
      return negative(value)

    if node.op == UnaryOperationEnum.NOT:
      return not_(value)

    raise Exception(f'Unknown unary operator: {node.op}')
