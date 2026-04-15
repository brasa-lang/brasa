from dataclasses import dataclass

@dataclass
class Value:
  pass

@dataclass
class IntegerValue(Value):
  value:int

@dataclass
class FloatValue(Value):
  value:float

@dataclass
class NullValue(Value):
  pass

@dataclass
class BooleanValue(Value):
  value:bool

@dataclass
class ArrayValue(Value):
  elements:list[Value]

@dataclass
class FunctionValue:
  params:any
  body:any
  return_type:any
  closure_scope:any
