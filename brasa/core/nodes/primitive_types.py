from dataclasses import dataclass

from brasa.core.types.types import Type

class IntegerType(Type): pass
class FloatType(Type): pass
class BooleanType(Type): pass
class StringType: pass

@dataclass
class NullableType(Type):
  base_type:Type
