from dataclasses import dataclass

@dataclass
class Literal:
  pass

@dataclass
class IntegerLiteral(Literal):
  value:int

@dataclass
class FloatLiteral(Literal):
  value:float

@dataclass
class NullLiteral(Literal):
  pass

@dataclass
class BooleanLiteral(Literal):
  value:bool

@dataclass
class ArrayLiteral(Literal):
  elements:list[any]

@dataclass
class FunctionValue:
  params:any
  body:any
  return_type:any
  closure_scope:any
