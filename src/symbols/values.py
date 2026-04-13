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
class ArrayValue(Value):
  elements: list[Value]

@dataclass
class NullValue(Value):
  pass
