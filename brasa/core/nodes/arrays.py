from dataclasses import dataclass

from brasa.core.types.values import Value
from brasa.core.types.types import Type

@dataclass
class ArrayType(Type):
  element_type:Type
  size:any

@dataclass
class ArrayValue(Value):
  elements:list[Value]
