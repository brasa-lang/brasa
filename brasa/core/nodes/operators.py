from dataclasses import dataclass

from brasa.core.types.operators import BinaryOperationEnum,UnaryOperationEnum

@dataclass
class BinaryOperation:
  left:any
  op:BinaryOperationEnum
  right:any

@dataclass
class UnaryOperation:
  op:UnaryOperationEnum
  expr:any
