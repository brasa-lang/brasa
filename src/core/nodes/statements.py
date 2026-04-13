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
  id:str
  type:Type
  expr:Literal
  is_const:bool

@dataclass
class UpdateVariableStatement:
  id:str
  expr:Literal

@dataclass
class PrintStatement:
  expr:Literal
