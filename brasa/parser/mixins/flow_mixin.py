from lark import v_args

from brasa.core.nodes.flow import IfStatement,WhileStatement,BreakStatement,ContinueStatement

class FlowMixin:
  @v_args(inline=True)
  def if_statement(
    self,
    condition,
    then_block,
    else_branch=None
  ):
    return IfStatement(
      condition,
      then_block,
      else_branch
    )

  @v_args(inline=True)
  def while_statement(
    self,
    condition,
    body
  ):
    return WhileStatement(condition,body)

  def break_statement(self,_): return BreakStatement()
  def continue_statement(self,_): return ContinueStatement()
