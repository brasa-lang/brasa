from brasa.core.nodes.primitive_values import IntegerValue,FloatValue,StringValue

from brasa.core.utils.types import is_int,is_float,is_string,is_number,is_null

def to_int(obj):
  if is_int(obj): return obj
  if is_float(obj): return IntegerValue(int(obj.value))

  if is_string(obj):
    try:
      return IntegerValue(int(obj.value))
    except ValueError:
      raise Exception(f'Cannot convert "{obj.value}" to int')

  raise Exception(f"Cannot convert {type(obj).__name__} to int")

def to_real(obj):
  if is_float(obj): return obj
  if is_int(obj): return FloatValue(float(obj.value))

  if is_string(obj):
    try:
      return FloatValue(float(obj.value))
    except ValueError:
      raise Exception(f'Cannot convert "{obj.value}" to real')

  raise Exception(f'Cannot convert {type(obj).__name__} to real')

def to_texto(obj):
  if is_string(obj): return obj
  if is_number(obj): return StringValue(str(obj.value))
  if is_null(obj): return StringValue('nulo')

exports={
  'int':to_int,
  'real':to_real,
  'texto':to_texto,
}
