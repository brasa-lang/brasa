from brasa.core.types.operators import BinaryOperationEnum,UnaryOperationEnum

from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,StringValue,NullValue,BooleanValue

class OperatorsMixin:
  def visit_BinaryOperation(self,node):
    op = node.op

    left = self.visit(node.left)
    right = self.visit(node.right)

    # -------- ARITHMETIC --------

    if op == BinaryOperationEnum.ADDITION:
      if isinstance(left, IntegerValue) and isinstance(right, IntegerValue):
        return IntegerValue(left.value + right.value)

      if isinstance(left, FloatValue) or isinstance(right, FloatValue):
        return FloatValue(float(left.value) + float(right.value))

      if isinstance(left, StringValue) or isinstance(right, StringValue):
        return StringValue(str(left.value) + str(right.value))

      raise Exception("Invalid types for +")

    if op == BinaryOperationEnum.SUBTRACTION:
      return FloatValue(left.value - right.value)

    if op == BinaryOperationEnum.MULTIPLICATION:
      return FloatValue(left.value * right.value)

    if op == BinaryOperationEnum.DIVISION:
      return FloatValue(left.value / right.value)

    # -------- COMPARISON --------

    if op == BinaryOperationEnum.GREATER_THAN:
      return BooleanValue(left.value > right.value)

    if op == BinaryOperationEnum.LESS_THAN:
      return BooleanValue(left.value < right.value)

    if op == BinaryOperationEnum.EQUAL:
      return BooleanValue(left.value == right.value)

    if op == BinaryOperationEnum.NOT_EQUAL:
      return BooleanValue(left.value != right.value)

    # -------- LOGIC --------

    if op == BinaryOperationEnum.AND:
      if not left.value:
        return BooleanValue(False)
      return BooleanValue(bool(right.value))

    if op == BinaryOperationEnum.OR:
      if left.value:
        return BooleanValue(True)
      return BooleanValue(bool(right.value))

    raise Exception(f'Unknown binary operator: {op}')

  def visit_UnaryOperation(self,node):
    value = self.visit(node.expr)

    if node.op == UnaryOperationEnum.NEGATIVE:
      return FloatValue(-value.value)

    if node.op == UnaryOperationEnum.NOT:
      return BooleanValue(not value.value)

    raise Exception(f'Unknown unary operator: {node.op}')
