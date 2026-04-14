from dataclasses import dataclass

from brasa.core.nodes.types import Type
from brasa.core.nodes.literals import Literal

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
class AssignStatement:
  id:str
  expr:Literal

@dataclass
class CompoundAssignStatement:
  id:any
  op:any
  expr:any

@dataclass
class PostfixStatement:
  id:str
  op:any

@dataclass
class PrintStatement:
  expr:Literal

@dataclass
class IfStatement:
  condition:any
  then_block:any
  else_branch:any

@dataclass
class Block:
  statements:any

@dataclass
class WhileStatement:
  condition:any
  body:any

@dataclass
class BreakStatement:
  pass

@dataclass
class ContinueStatement:
  pass
