from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,BooleanValue
from brasa.core.utils.types import is_int,is_float,is_bool

def error_unary_operator(
  op,
  operand
):
  raise Exception(f'operator "{op}" has no support to "{operand}"')

def negative(operand):
  if is_int(operand):
    return IntegerValue(operand.value*-1)

  if is_float(operand):
    return FloatValue(operand.value*-1)

  error_unary_operator(
    op='-',
    operand=operand
  )

def not_(operand):
  if is_bool(operand):
    return BooleanValue(not operand.value)

  error_unary_operator(
    op='!',
    operand=operand
  )
