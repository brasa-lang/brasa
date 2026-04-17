from brasa.core.utils.conversions import to_python

def diga(prompt):
  print(to_python(prompt))

def leia():
  return input()

exports={
  'diga':diga,
  'leia':leia,
}
