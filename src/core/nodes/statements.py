from dataclasses import dataclass

from src.core.nodes.types import Type
from src.core.nodes.literals import Literal

@dataclass
class Program:
  statements:list[any]

@dataclass
class Identifier:
  name:str

@dataclass
class VarDeclarationStatement:
  name:str
  type:Type
  value:Literal
  is_const:bool
