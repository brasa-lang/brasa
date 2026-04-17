from brasa.core.nodes.primitive_values import IntegerValue,StringValue
from brasa.core.nodes.arrays import ArrayValue

from brasa.core.utils.index import index_array,index_string

class ArrayMixins:
  def visit_ArrayValue(self,node):
    return [self.visit(elem) for elem in node.elements]

  def visit_IndexExpression(self,node):
    arr=self.visit(node.base)
    index=self.visit(node.index)

    if not isinstance(index,IntegerValue):
      raise Exception('Index must be an int')

    if isinstance(node.base,ArrayValue):
        return index_array(node.base,index)

    elif isinstance(node.base,StringValue):
        return index_string(node.base,index)

    return arr[index.value]
