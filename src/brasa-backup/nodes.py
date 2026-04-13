from dataclasses import dataclass
from typing import List, Any

@dataclass
class Node:
  pass

@dataclass
class LiteralNode(Node):
  value: Any

@dataclass
class VarLookupNode(Node):
  name: str

@dataclass
class BinOpNode(Node):
  left: Node
  op: str
  right: Node

@dataclass
class DeclarationNode(Node):
  var_type: str
  name: str
  value: Node

@dataclass
class AssignmentNode(Node):
  name: str
  value: Node

@dataclass
class PrintNode(Node):
  value: Node

@dataclass
class ProgramNode(Node):
  statements: List[Node]

@dataclass
class IncrementNode(Node):
  name: str

@dataclass
class DecrementNode(Node):
  name: str

@dataclass
class IfNode(Node):
  condition:Node
  then_block:List[Node]
  else_block:List[Node]=None

@dataclass
class WhileNode(Node):
  condition:Node
  block:List[Node]

@dataclass
class UnaryMinusNode(Node):
  expr: Node
