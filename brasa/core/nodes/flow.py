from dataclasses import dataclass

@dataclass
class IfStatement:
  condition:any
  then_block:any
  else_branch:any

@dataclass
class WhileStatement:
  condition:any
  body:any

class BreakStatement: pass
class ContinueStatement: pass
