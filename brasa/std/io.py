from brasa.core.utils.conversions import to_python

from brasa.core.nodes.primitive_values import StringValue

def diga(prompt):
  print(to_python(prompt))

def leia():
  return StringValue(value=input())

exports={
  'diga':diga,
  'leia':leia,
}
