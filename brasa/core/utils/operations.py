from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,StringValue,BooleanValue

def add(left,right):
  if isinstance(left, IntegerValue) and isinstance(right, IntegerValue):
    return IntegerValue(left.value + right.value)

  if isinstance(left, FloatValue) or isinstance(right, FloatValue):
    return FloatValue(float(left.value) + float(right.value))

  if isinstance(left, StringValue) or isinstance(right, StringValue):
    return StringValue(str(left.value) + str(right.value))

  raise Exception("Invalid types for +")

def sub(left,right):
  return FloatValue(left.value - right.value)

def mul(left,right):
  return FloatValue(left.value * right.value)

def div(left,right):
  return FloatValue(left.value / right.value)

def greater_than(left,right):
  return BooleanValue(left.value > right.value)

def less_than(left,right):
  return BooleanValue(left.value < right.value)

def equal(left,right):
  return BooleanValue(left.value == right.value)

def not_equal(left,right):
  return BooleanValue(left.value != right.value)

def and_(left,right):
  if not left.value:
    return BooleanValue(False)

  return BooleanValue(bool(right.value))

def or_(left,right):
  if left.value:
    return BooleanValue(True)

  return BooleanValue(bool(right.value))

def negative(value):
  return FloatValue(-value.value)

def not_(value):
  return BooleanValue(not value.value)
