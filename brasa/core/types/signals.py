from dataclasses import dataclass

class BreakSignal(Exception): pass
class ContinueSignal(Exception): pass

@dataclass
class ReturnSignal(Exception):
  value:any
