from dataclasses import dataclass

@dataclass
class Type:
  pass

@dataclass
class IntegerType(Type):
  pass

@dataclass
class FloatType(Type):
  pass

@dataclass
class NullableType(Type):
  base_type:Type

@dataclass
class ArrayType(Type):
  element_type:Type
  size:int
