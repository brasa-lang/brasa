from core.nodes.types import Type
from src.symbols.values import Value

class World:
  TypeComponent: dict[int, Type]
  ValueComponent: dict[int, Value]
  ConstComponent: set[int]
