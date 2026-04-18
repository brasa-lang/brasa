from brasa.core.nodes.primitive_values import IntegerValue,StringValue
from brasa.core.nodes.arrays import ArrayValue

from brasa.core.utils.index import index_array,index_string

class ArrayMixins:
  def visit_ArrayValue(self,node): return node

  def visit_IndexExpression(self,node):
    arr=self.visit(node.base)
    index=self.visit(node.index)

    print(f'node: {arr}')

    if not isinstance(index,IntegerValue): raise Exception('Index must be an int')

    if isinstance(arr,ArrayValue): return index_array(arr,index)
    elif isinstance(arr,StringValue): return index_string(arr,index)

    raise Exception(f'{arr} is not indexable')
