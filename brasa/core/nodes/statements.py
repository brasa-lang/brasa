from dataclasses import dataclass

from brasa.core.nodes.types import Type
from brasa.core.nodes.values import Value

# ---------------- VARIABLES ----------------

@dataclass
class VariableDeclarationStatement:
  id:str
  type:Type
  expr:Value
  is_const:bool

@dataclass
class AssignmentStatement:
  id:str
  expr:Value

@dataclass
class CompoundAssignmentStatement:
  id:any
  op:any
  expr:any

@dataclass
class PostfixStatement:
  id:str
  op:any

# ---------------- CONTROL FLOW ----------------

@dataclass
class IfStatement:
  condition:any
  then_block:any
  else_branch:any

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

# ---------------- FUNCTIONS ----------------

@dataclass
class FunctionDeclaration:
  name:str
  params:any
  return_type:any
  body:any

@dataclass
class LambdaExpression:
  params:any
  return_type:any
  body:any

@dataclass
class CallExpression:
  callee:any
  args:any

@dataclass
class ReturnStatement:
  expr:any

# ---------------- REMOVE LATER ----------------

@dataclass
class PrintStatement:
  expr:Value
