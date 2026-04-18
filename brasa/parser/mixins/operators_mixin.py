from lark import v_args

from brasa.core.nodes.operators import BinaryOperation,UnaryOperation
from brasa.core.types.operators import BinaryOperationEnum,UnaryOperationEnum
from brasa.core.nodes.variables import PostfixStatement

class OperatorsMixin:
  @v_args(inline=True)
  def OP_ASSIGN(self,token):
    return {
      '+=':BinaryOperationEnum.ADDITION,
      '-=':BinaryOperationEnum.SUBTRACTION,
      '*=':BinaryOperationEnum.MULTIPLICATION,
      '/=':BinaryOperationEnum.DIVISION,
      '%=':BinaryOperationEnum.REMAINDER,
    }[token]

  @v_args(inline=True)
  def OP_POSTFIX(self,token):
    if token=='++': return BinaryOperationEnum.ADDITION
    return BinaryOperationEnum.SUBTRACTION

  @v_args(inline=True)
  def add(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.ADDITION,
      right
    )

  @v_args(inline=True)
  def sub(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.SUBTRACTION,
      right
    )

  @v_args(inline=True)
  def mul(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.MULTIPLICATION,
      right
    )

  @v_args(inline=True)
  def div(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.DIVISION,
      right
    )

  @v_args(inline=True)
  def remainder(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.REMAINDER,
      right
    )

  @v_args(inline=True)
  def neg(self,value):
    return UnaryOperation(
      UnaryOperationEnum.NEGATIVE,
      value
    )

  @v_args(inline=True)
  def greater_than(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.GREATER_THAN,
      right
    )

  @v_args(inline=True)
  def less_than(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.LESS_THAN,
      right
    )

  @v_args(inline=True)
  def greater_than_or_equal_to(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.GREATER_THAN_OR_EQUAL_TO,
      right
    )

  @v_args(inline=True)
  def less_than_or_equal_to(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.LESS_THAN_OR_EQUAL_TO,
      right
    )

  @v_args(inline=True)
  def equal(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.EQUAL,
      right
    )

  @v_args(inline=True)
  def not_equal(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.NOT_EQUAL,
      right
    )

  @v_args(inline=True)
  def and_op(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.AND,
      right
    )

  @v_args(inline=True)
  def or_op(self,left,right):
    return BinaryOperation(
      left,
      BinaryOperationEnum.OR,
      right
    )

  @v_args(inline=True)
  def not_op(self,value):
    return UnaryOperation(
      UnaryOperationEnum.NOT,
      value
    )

  @v_args(inline=True)
  def postfix(self,target,op):
    return PostfixStatement(
      lvalue=target,
      op=op
    )
