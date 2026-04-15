from lark import v_args

from brasa.core.nodes.primitive_types import IntegerType,FloatType,BooleanType,StringType,NullableType

class PrimitiveTypesMixin:
  def int_type(self,_): return IntegerType()
  def float_type(self,_): return FloatType()
  def bool_type(self, _): return BooleanType()
  def string_type(self,_): return StringType()

  @v_args(inline=True)
  def nullable_type(self,type):
    return NullableType(base_type=type)
