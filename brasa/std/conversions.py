from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,StringValue,NullValue

def to_int(value):
  print(f'test: {value}') # This is not a class

  # already int
  if isinstance(value, IntegerValue):
    return value

  # real → int
  if isinstance(value, FloatValue):
    return IntegerValue(int(value.value))

  # string → int
  if isinstance(value, StringValue):
      try:
          return IntegerValue(int(value.value))
      except ValueError:
          raise Exception(f'Cannot convert "{value.value}" to int')

  raise Exception(f"Cannot convert {type(value).__name__} to int")

exports={
  'to_int':to_int
}
