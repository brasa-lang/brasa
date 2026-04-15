from dataclasses import dataclass

from brasa.core.types.values import Value

@dataclass
class IntegerValue(Value):
  value:int

@dataclass
class FloatValue(Value):
  value:float

@dataclass
class BooleanValue(Value):
  value:bool

@dataclass
class StringValue:
  value:str

@dataclass
class NullValue(Value): pass
