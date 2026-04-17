from brasa.core.utils.print import to_python

from brasa.core.nodes.primitive_values import StringValue

def diga(text=''):
  print(
    to_python(text),
    end=''
  )

def diga_nl(text=''):
  print(to_python(text))

def leia():
  return StringValue(value=input())

exports={
  'diga':diga,
  'diga_nl':diga_nl,
  'leia':leia,
}
