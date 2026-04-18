from brasa.core.utils.print import to_python

from brasa.core.nodes.primitive_values import StringValue
from brasa.core.nodes.functions import VoidValue

def diga(obj=''):
  print(
    to_python(obj),
    end=''
  )

  return VoidValue()

def diga_nl(obj=''):
  print(to_python(obj))

  return VoidValue()

def leia(): return StringValue(value=input())

exports={
  'diga':diga,
  'diga_nl':diga_nl,
  'leia':leia,
}
