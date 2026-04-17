from brasa.core.types.operators import BinaryOperationEnum,UnaryOperationEnum

from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,StringValue,NullValue,BooleanValue

from brasa.core.utils.operations import add,sub,mul,div,greater_than,less_than,equal,not_equal,and_,or_,negative,not_

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

    # -------- COMPARISON --------

    if op == BinaryOperationEnum.GREATER_THAN:
      return greater_than(left,right)

    if op == BinaryOperationEnum.LESS_THAN:
      return less_than(left,right)

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
