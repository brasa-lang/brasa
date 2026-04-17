from lark import v_args

from brasa.core.nodes.basics import Identifier

from brasa.core.nodes.primitive_values import NullValue
from brasa.core.types.lvalues import VarLValue,IndexLValue

from brasa.core.nodes.variables import VariableDeclarationStatement,AssignmentStatement,CompoundAssignmentStatement

class VariablesMixin:
  @v_args(inline=True)
  def variable_lvalue(self,target):
    return VarLValue(name=target.name)

  @v_args(inline=True)
  def index_lvalue(
    self,
    base,
    index
  ):
    return IndexLValue(
      base=base,
      index=index
    )

  def ID(self,name):
    return Identifier(name=str(name))

  @v_args(inline=True)
  def variable_declaration(
    self,
    const_keyword,
    var_type,
    id,
    expr
  ):
    return VariableDeclarationStatement(
      id=id,
      type=var_type,
      expr=NullValue() if expr is None else expr,
      is_const=const_keyword is not None
    )

  @v_args(inline=True)
  def assignment(
    self,
    target,
    expr
  ):
    return AssignmentStatement(
      target=target,
      expr=expr
    )

  @v_args(inline=True)
  def compound_assignment(
    self,
    target,
    op,
    expr
  ):
    return CompoundAssignmentStatement(
      target=target,
      op=op,
      expr=expr
    )
