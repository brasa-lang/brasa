from lark import v_args

from brasa.core.nodes.basics import Program,Block,PrintStatement

class BasicsMixin:
  def program(self,statements):
    return Program(statements=statements)

  @v_args(inline=True)
  def statement(self,item):
    return item

  def block(self,statements):
    return Block(list(statements))

  @v_args(inline=True)
  def print_variable(self,expr):
    return PrintStatement(expr)
