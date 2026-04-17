from lark import v_args

from brasa.core.nodes.functions import FunctionType,FunctionDeclarationStatement,VoidType,CallExpression,ReturnStatement,LambdaExpression

class FunctionsMixin:
  @v_args(inline=True)
  def function_declaration(
    self,
    name,
    parameters,
    return_type,
    body
  ):
    return FunctionDeclarationStatement(
      name=name,
      params=[] if parameters is None else parameters,
      return_type=VoidType() if return_type is None else return_type,
      body=body
    )

  def void_type(self,_): return VoidType()

  @v_args(inline=True)
  def func_type(
    self,
    parameters=None,
    return_type=None
  ):
    if parameters is None:
      parameters=[]

    return FunctionType(
      parameters,
      return_type
    )

  @v_args(inline=True)
  def call(self,callee,args=None):
    return CallExpression(
      callee=callee,
      args=[] if args is None else args
    )

  @v_args(inline=True)
  def return_type(self,type): return type

  def args_list(self,params): return params
  def param_list(self,params): return params

  @v_args(inline=True)
  def param(self,type,name): return (type,name)

  @v_args(inline=True)
  def return_statement(self,expr=None):
    return ReturnStatement(expr)

  @v_args(inline=True)
  def lambda_expr(
    self,
    parameters,
    return_type,
    body
  ):
    if parameters is None:
      parameters=[]

    if return_type is None:
      return_type=VoidType()

    return LambdaExpression(
      parameters=parameters,
      return_type=return_type,
      body=body
    )
