from dataclasses import dataclass

from brasa.core.types.values import Value
from brasa.core.types.types import Type

@dataclass
class FunctionType(Type):
  param_types:list[Type]
  return_type:Type

@dataclass
class FunctionValue(Value):
  params:any
  body:any
  return_type:any
  closure_scope:any

class VoidType(Type): pass
class VoidValue(Value): pass

@dataclass
class FunctionDeclarationStatement:
  name:str
  params:any
  return_type:any
  body:any

@dataclass
class CallExpression:
  callee:any
  args:any

@dataclass
class ReturnStatement:
  expr:any

@dataclass
class LambdaExpression:
  parameters:any
  return_type:any
  body:any
