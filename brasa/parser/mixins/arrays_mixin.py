from lark import v_args

from brasa.core.nodes.arrays import ArrayType,ArrayValue,IndexExpression

class ArrayMixin:
  @v_args(inline=True)
  def array_type(self,element_type,size):
    return ArrayType(
      element_type=element_type,
      size=size
    )

  @v_args(inline=True)
  def array_value(self,*elements):
    if len(elements)==1 and elements[0] is None:
      elements=[]

    return ArrayValue(elements=elements)

  @v_args(inline=True)
  def index_expr(self,obj,index):
    return IndexExpression(obj,index)
