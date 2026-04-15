class PrimitiveValuesMixin:
  def visit_IntegerValue(self,node): return node.value
  def visit_FloatValue(self,node): return node.value
  def visit_BooleanValue(self,node): return node.value
  def visit_StringValue(self,node): return node.value
  def visit_NullValue(self,_): return None
