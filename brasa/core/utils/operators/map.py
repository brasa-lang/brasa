from brasa.core.types.operators import *
from brasa.core.utils.operators.binary import *
from brasa.core.utils.operators.unary import *

BINARY_OPS_MAP={
  BinaryOperationEnum.ADDITION:add,
  BinaryOperationEnum.SUBTRACTION:sub,
  BinaryOperationEnum.MULTIPLICATION:mul,
  BinaryOperationEnum.DIVISION:div,
  BinaryOperationEnum.REMAINDER:remainder,

  BinaryOperationEnum.GREATER_THAN:greater_than,
  BinaryOperationEnum.LESS_THAN:less_than,
  BinaryOperationEnum.GREATER_THAN_OR_EQUAL_TO:greater_than_or_equal_to,
  BinaryOperationEnum.LESS_THAN_OR_EQUAL_TO:less_than_or_equal_to,
  BinaryOperationEnum.EQUAL:equal,
  BinaryOperationEnum.NOT_EQUAL:not_equal,

  BinaryOperationEnum.AND:and_,
  BinaryOperationEnum.OR:or_,
}

UNARY_OPS_MAP={
  UnaryOperationEnum.NEGATIVE:negative,
  UnaryOperationEnum.NOT:not_,
}
