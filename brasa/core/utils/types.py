from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,StringValue,BooleanValue,NullValue

def is_int(value)->bool:
  return isinstance(value,IntegerValue)

def is_float(value)->bool:
  return isinstance(value,FloatValue)

def is_number(value)->bool:
  return is_int(value) or is_float(value)

def is_bool(value)->bool:
  return isinstance(value,BooleanValue)

def is_string(value)->bool:
  return isinstance(value,StringValue)

def is_null(value)->bool:
  return isinstance(value,NullValue)
