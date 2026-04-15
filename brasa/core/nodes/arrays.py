from dataclasses import dataclass

from brasa.core.types.values import Value
from brasa.core.types.types import Type

@dataclass
class ArrayType(Type):
  element_type:any
  size:any

@dataclass
class ArrayValue(Value):
  elements:list[Value]

@dataclass
class IndexExpression:
  base:any
  index:any
