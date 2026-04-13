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
