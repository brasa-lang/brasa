from enum import Enum, auto

class BinaryOperationEnum(Enum):
  ADD = auto()
  SUB = auto()
  MUL = auto()
  DIV = auto()

  GT = auto()
  LT = auto()
  GE = auto()
  LE = auto()
  EQ = auto()
  NE = auto()

  AND = auto()
  OR = auto()

class UnaryOperationEnum(Enum):
  NEG = auto()
  NOT = auto()
