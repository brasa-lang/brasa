class PrimitiveValuesMixin:
  def visit_IntegerValue(self,node): return node
  def visit_FloatValue(self,node): return node
  def visit_BooleanValue(self,node): return node
  def visit_StringValue(self,node): return node
  def visit_NullValue(self,node): return node
