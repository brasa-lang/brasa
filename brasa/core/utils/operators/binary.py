from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,StringValue,BooleanValue

from brasa.core.utils.types import is_int,is_number,is_string,is_bool

def error_binary_operator(
  op,
  left_operand_type,
  right_operand_type
):
  raise Exception(f'unsupported operand types for "{op}": "{left_operand_type}" and "{right_operand_type}"')

def add(left,right):
  if is_int(left) and is_int(right):
    return IntegerValue(left.value+right.value)

  if is_number(left) and is_number(right):
    return FloatValue(left.value+right.value)

  if is_string(left) and is_string(right):
    return StringValue(str(left.value)+str(right.value))

  error_binary_operator(
    op='+',
    left_operand_type=left,
    right_operand_type=right
  )

def sub(left,right):
  if is_int(left) and is_int(right):
    return IntegerValue(left.value-right.value)

  if is_number(left) and is_number(right):
    return FloatValue(left.value-right.value)

  error_binary_operator(
    op='-',
    left_operand_type=left,
    right_operand_type=right
  )

def mul(left,right):
  if is_int(left) and is_int(right):
    return IntegerValue(left.value*right.value)

  if is_number(left) and is_number(right):
    return FloatValue(left.value*right.value)

  error_binary_operator(
    op='*',
    left_operand_type=left,
    right_operand_type=right
  )

def div(left,right):
  if is_number(left) and is_number(right):
    if right.value==0:
      raise Exception('Division by zero')

    return FloatValue(left.value/right.value)

  error_binary_operator(
    op='/',
    left_operand_type=left,
    right_operand_type=right
  )

def remainder(left,right):
  if is_int(left) and is_int(right):
    return IntegerValue(left.value%right.value)

  if is_number(left) and is_number(right):
    return FloatValue(left.value%right.value)

  error_binary_operator(
    op='%',
    left_operand_type=left,
    right_operand_type=right
  )

def greater_than(left,right):
  if is_number(left) and is_number(right):
    return BooleanValue(left.value>right.value)

  error_binary_operator(
    op='>',
    left_operand_type=left,
    right_operand_type=right
  )

def less_than(left,right):
  if is_number(left) and is_number(right):
    return BooleanValue(left.value<right.value)

  error_binary_operator(
    op='<',
    left_operand_type=left,
    right_operand_type=right
  )

def less_than_or_equal_to(left,right):
  if is_number(left) and is_number(right):
    return BooleanValue(left.value<=right.value)

  error_binary_operator(
    op='<=',
    left_operand_type=left,
    right_operand_type=right
  )

def greater_than_or_equal_to(left,right):
  if is_number(left) and is_number(right):
    return BooleanValue(left.value>=right.value)

  error_binary_operator(
    op='>=',
    left_operand_type=left,
    right_operand_type=right
  )

def equal(left,right):
  if is_number(left) and is_number(right):
    return BooleanValue(left.value==right.value)

  error_binary_operator(
    op='==',
    left_operand_type=left,
    right_operand_type=right
  )

def not_equal(left,right):
  if is_number(left) and is_number(right):
    return BooleanValue(left.value!=right.value)

  error_binary_operator(
    op='!=',
    left_operand_type=left,
    right_operand_type=right
  )

def and_(left,right):
  if is_bool(left) and is_bool(right):
    return BooleanValue(left.value and right.value)

  error_binary_operator(
    op='and',
    left_operand_type=left,
    right_operand_type=right
  )

def or_(left,right):
  if is_bool(left) and is_bool(right):
    return BooleanValue(left.value or right.value)

  error_binary_operator(
    op='or',
    left_operand_type=left,
    right_operand_type=right
  )
