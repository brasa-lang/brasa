from dataclasses import dataclass

@dataclass
class IfStatement:
  condition:any
  then_block:list[any]
  else_branch:list[any]

@dataclass
class WhileStatement:
  condition:any
  body:list[any]

@dataclass
class BreakStatement: pass

@dataclass
class ContinueStatement: pass
