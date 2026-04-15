from lark import Transformer,v_args

from brasa.core.nodes.basics import *
from brasa.core.nodes.statements import *
from brasa.core.nodes.types import *
from brasa.core.nodes.values import *
from brasa.core.types.lvalues import *

from brasa.core.nodes.operators import BinaryOperation,UnaryOperation
from brasa.core.types.operators import BinaryOperationEnum,UnaryOperationEnum

class ASTBuilder(Transformer):
  # ---------------- PROGRAM ----------------

  def program(self,statements):
    return Program(statements=statements)

  @v_args(inline=True)
  def statement(self, item):
    return item

  def block(self,statements):
    return Block(list(statements))

  # ---------------- VARIABLES ----------------

  def ID(self,name):
    return Identifier(name=str(name))

  @v_args(inline=True)
  def var_declaration(self,const,type_,id,expr):
    return VariableDeclarationStatement(
      id=id,
      type=type_,
      expr=expr,
      is_const=const is not None
    )

  @v_args(inline=True)
  def var_declaration_null(self,const,type_,id):
    return VariableDeclarationStatement(
      id=id,
      type=type_,
      expr=NullValue(),
      is_const=const is not None
    )

  @v_args(inline=True)
  def assigment(self,id,expr):
    return AssignmentStatement(
      target=id,
      expr=expr
    )

  @v_args(inline=True)
  def compound_assignment(self,id,op,expr):
    return CompoundAssignmentStatement(
      target=id,
      op=op,
      expr=expr
    )

  @v_args(inline=True)
  def postfix(self,id,op):
    return PostfixStatement(
      target=id,
      op=op
    )

  def OP_POSTFIX(self, token):
    return token.value

  @v_args(inline=True)
  def var_lvalue(self, id_):
    return VarLValue(id_.name)


  @v_args(inline=True)
  def index_lvalue(self, base, index):
    return IndexLValue(base, index)

  # ---------------- TYPES ----------------

  def int_type(self,_):
    return IntegerType()

  def float_type(self,_):
    return FloatType()

  @v_args(inline=True)
  def nullable_type(self,type_):
    return NullableType(base_type=type_)

  def string_type(self,_):
    return StringType()

  def bool_type(self, _):
    return BooleanType()

  def void_type(self, _):
    return VoidType()

  @v_args(inline=True)
  def array_type(self,element_type,size):
    return ArrayType(
      element_type=element_type,
      size=size
    )

  # ---------------- LITERALS ----------------

  @v_args(inline=True)
  def integer_literal(self,value):
    return IntegerValue(value=int(value))

  @v_args(inline=True)
  def float_literal(self,value):
    return FloatValue(value=float(value))

  @v_args(inline=True)
  def string_literal(self, token):
    return StringLiteral(value=token[1:-1])

  def null_literal(self,_):
    return NullValue()

  def true_literal(self, _):
    return BooleanValue(True)

  def false_literal(self, _):
    return BooleanValue(False)

  @v_args(inline=True)
  def array_literal(self,*elements):
    if len(elements)==1 and elements[0] is None:
      elements=[]

    return ArrayValue(elements=elements)

  @v_args(inline=True)
  def index_expr(self, base, index):
    return IndexExpression(base, index)

  # ---------------- CONTROL FLOW ----------------

  @v_args(inline=True)
  def if_statement(self, cond, then_block, else_branch=None):
    return IfStatement(cond, then_block, else_branch)

  @v_args(inline=True)
  def while_statement(self, condition, body):
    return WhileStatement(condition, body)

  def break_statement(self, _):
    return BreakStatement()

  def continue_statement(self, _):
    return ContinueStatement()

  # ---------------- OPERATORS ----------------

  # ---------------- MATH ----------------

  @v_args(inline=True)
  def add(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.ADD, right)

  @v_args(inline=True)
  def sub(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.SUB, right)

  @v_args(inline=True)
  def mul(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.MUL, right)

  @v_args(inline=True)
  def div(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.DIV, right)

  @v_args(inline=True)
  def neg(self, value):
      return UnaryOperation(UnaryOperationEnum.NEG, value)

  @v_args(inline=True)
  def OP_ASSIGN(self, token):
    return {
      '+=': BinaryOperationEnum.ADD,
      '-=': BinaryOperationEnum.SUB,
      '*=': BinaryOperationEnum.MUL,
      '/=': BinaryOperationEnum.DIV,
    }[token]

  @v_args(inline=True)
  def OP_POSTFIX(self, token):
    if token=='++':
      return BinaryOperationEnum.ADD

    return BinaryOperationEnum.SUB

  # ---------------- COMPARISONS ----------------

  @v_args(inline=True)
  def gt(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.GT, right)

  @v_args(inline=True)
  def lt(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.LT, right)

  @v_args(inline=True)
  def ge(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.GE, right)

  @v_args(inline=True)
  def le(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.LE, right)

  @v_args(inline=True)
  def eq(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.EQ, right)

  @v_args(inline=True)
  def ne(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.NE, right)

  # ---------------- LOGICAL ----------------

  @v_args(inline=True)
  def and_op(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.AND, right)

  @v_args(inline=True)
  def or_op(self, left, right):
    return BinaryOperation(left, BinaryOperationEnum.OR, right)

  @v_args(inline=True)
  def not_op(self, value):
    return UnaryOperation(UnaryOperationEnum.NOT, value)

  # ---------------- FUNCTION ----------------

  @v_args(inline=True)
  def func_declaration(self,func_name,parameters,return_type,block):
    return FunctionDeclaration(
      name=func_name,
      params=[] if parameters is None else parameters,
      return_type=VoidType() if return_type is None else return_type,
      body=block
    )

  @v_args(inline=True)
  def func_type(self, params=None, return_type=None):
    if params is None:
      params = []
    return FunctionType(params, return_type)

  @v_args(inline=True)
  def call_func(self,id,parameters):
    return CallExpression(
      callee=id,
      args=[] if parameters is None else parameters
    )

  @v_args(inline=True)
  def return_type(self, type_):
    return type_

  def args_list(self, params):
    return params

  def param_list(self, params):
    return params

  @v_args(inline=True)
  def param(self, type_, name):
    return (type_, name)

  @v_args(inline=True)
  def return_statement(self, expr=None):
    return ReturnStatement(expr)

  @v_args(inline=True)
  def lambda_expr(self, params=None, return_type=None, body=None):
    if params is None:
      params = []

    if return_type is None:
      return_type = VoidType()

    return LambdaExpression(
      params=params,
      return_type=return_type,
      body=body
    )

  # ---------------- REMOVE LATER ----------------

  @v_args(inline=True)
  def print_variable(self,expr):
    return PrintStatement(expr)
