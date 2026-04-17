class ArrayMixins:
  def visit_ArrayValue(self,node):
    return [self.visit(elem) for elem in node.elements]

  def visit_IndexExpression(self,node):
    arr=self.visit(node.base)
    index=self.visit(node.index)

    return arr[index]
