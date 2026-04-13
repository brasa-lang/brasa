from dataclasses import dataclass

from src.core.utils.operators import BinOp

@dataclass
class BinaryOp:
  left:any
  op:BinOp
  right:any
