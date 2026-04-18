from dataclasses import dataclass

from brasa.core.runtime.scope import Scope
from brasa.core.types.values import Value
from brasa.core.types.types import Type

@dataclass
class VoidType(Type): pass

@dataclass
class VoidValue(Value): pass

@dataclass
class FunctionType(Type):
  param_types:list[Type]
  return_type:Type

@dataclass
class FunctionValue(Value):
  params:list[any]
  return_type:Type
  body:list[any]
  closure_scope:Scope

@dataclass
class FunctionDeclarationStatement:
  name:str
  params:list[any]
  return_type:Type
  body:list[any]

@dataclass
class CallExpression:
  callee:any
  args:list[any]

@dataclass
class ReturnStatement:
  expr:any

@dataclass
class LambdaExpression:
  params:list[any]
  return_type:Type
  body:list[any]

@dataclass
class BuiltinFunction:
  name:Type
  func:any
