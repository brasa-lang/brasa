from lark import Transformer,v_args

from src.core.nodes.statements import *
from src.core.nodes.types import *
from src.core.nodes.literals import *

class ASTBuilder(Transformer):
  # ---------------- PROGRAM ----------------

  def program(self,statements):
    return Program(statements=statements)

  @v_args(inline=True)
  def statement(self, item):
    return item

  # ---------------- VARIABLES ----------------

  def ID(self,name):
    return Identifier(name=str(name))

  @v_args(inline=True)
  def var_declaration(self,const,type_,id,expr):
    return VarDeclarationStatement(
      id=id,
      type=type_,
      expr=expr,
      is_const=const is not None
    )

  @v_args(inline=True)
  def var_declaration_null(self,const,type_,id):
    return VarDeclarationStatement(
      id=id,
      type=type_,
      expr=NullLiteral(),
      is_const=const is not None
    )

  @v_args(inline=True)
  def update_variable(self,id,expr):
    return UpdateVariableStatement(
      id=id,
      expr=expr
    )

  @v_args(inline=True)
  def print_variable(self,expr):
    return PrintStatement(expr)

  # ---------------- TYPES ----------------

  def int_type(self,_):
    return IntegerType()

  def float_type(self,_):
    return FloatType()

  @v_args(inline=True)
  def nullable_type(self,type_):
    return NullableType(base_type=type_)

  @v_args(inline=True)
  def array_type(self,element_type,size):
    return ArrayType(
      element_type=element_type,
      size=size
    )

  # ---------------- LITERALS ----------------

  @v_args(inline=True)
  def integer_literal(self,value):
    return IntegerLiteral(value=int(value))

  @v_args(inline=True)
  def float_literal(self,value):
    return FloatLiteral(value=float(value))

  def null_literal(self,_):
    return NullLiteral()

  @v_args(inline=True)
  def array_literal(self,*elements):
    if len(elements)==1 and elements[0] is None:
      elements=[]

    return ArrayLiteral(elements=elements)
