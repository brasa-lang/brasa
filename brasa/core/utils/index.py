from brasa.core.nodes.primitive_values import IntegerValue,StringValue
from brasa.core.nodes.arrays import ArrayValue

def index_array(
  arr:ArrayValue,
  index:IntegerValue
):
  index=index.value
  elements=arr.elements

  if index<0 or index>=len(elements):
    raise Exception('Array index out of bounds')

  return elements[index]

def index_string(
  string:StringValue,
  index:IntegerValue
):
  i=index.value
  value=string.value

  if i<0 or i>=len(value):
    raise Exception('String index out of bounds')

  return StringValue(value[i])
