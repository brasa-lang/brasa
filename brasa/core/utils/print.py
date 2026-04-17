from brasa.core.utils.types import is_number,is_bool,is_string,is_null

def to_python(obj):
  if is_number(obj):
    return obj.value

  if is_string(obj):
    return obj.value

  if is_bool(obj):
    if obj.value is True:
      return 'verdadeiro'

    return 'falso'

  if is_null(obj):
    return 'nulo'

  return obj
