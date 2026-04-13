from dataclasses import dataclass
from typing import Any, Optional, List

@dataclass
class Node:
  pass

@dataclass
class ProgramNode(Node):
  statements: List[Node]

@dataclass
class VarDeclarationNode(Node):
  name: str
  type_name: str
  initial_value: Optional[Any]
  is_const: bool
  is_nullable: bool

@dataclass
class UpdateVarNode:
  name: str
  expression: Any

@dataclass
class PrintNode(Node):
  expression: Any

@dataclass
class IdentifierNode(Node):
  name: Any

@dataclass
class LiteralNode(Node):
  value: Any
