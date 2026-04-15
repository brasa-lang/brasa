from dataclasses import dataclass

from brasa.core.nodes.primitive_types import Type
from brasa.core.nodes.primitive_values import Value

@dataclass
class VariableDeclarationStatement:
  id:str
  type:Type
  expr:Value
  is_const:bool

@dataclass
class AssignmentStatement:
  target:str
  expr:Value

@dataclass
class CompoundAssignmentStatement:
  target:any
  op:any
  expr:any

@dataclass
class PostfixStatement:
  target:any
  op:any
