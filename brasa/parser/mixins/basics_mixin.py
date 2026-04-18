from lark import v_args

from brasa.core.nodes.basics import Program,Block

class BasicsMixin:
  def program(self,statements):
    return Program(statements=statements)

  @v_args(inline=True)
  def statement(self,item):
    return item

  def block(self,statements):
    return Block(list(statements))
