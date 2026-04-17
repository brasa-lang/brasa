def diga(texto,prefix=''):
  print(123)
  print(f'{prefix}{texto}')

def leia():
  return input()

exports={
  'diga':diga,
  'leia':leia,
}
