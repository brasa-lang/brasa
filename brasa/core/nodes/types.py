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
class StringType:
  pass

@dataclass
class NullableType(Type):
  base_type:Type

@dataclass
class BooleanType(Type):
  pass

@dataclass
class ArrayType(Type):
  element_type:Type
  size:int

@dataclass
class VoidType(Type):
  pass

@dataclass
class FunctionType(Type):
  param_types:list[Type]
  return_type:Type
