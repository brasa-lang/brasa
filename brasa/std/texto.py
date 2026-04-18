from brasa.core.nodes.primitive_values import IntegerValue,StringValue

def tamanho(t:StringValue): return IntegerValue(len(t.value))
def maiusculo(t:StringValue): return StringValue(t.value.upper())
def minusculo(t:StringValue): return StringValue(t.value.lower())

exports={
  'tamanho':tamanho,
  'maiusculo':maiusculo,
  'minusculo':minusculo
}
