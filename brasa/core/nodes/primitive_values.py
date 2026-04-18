from dataclasses import dataclass

from brasa.core.types.values import Value

@dataclass
class IntegerValue(Value):
  value:int
  def __str__(self): return 'int'

@dataclass
class FloatValue(Value):
  value:float
  def __str__(self): return 'real'

@dataclass
class BooleanValue(Value):
  value:bool
  def __str__(self): return 'logico'

@dataclass
class StringValue:
  value:str
  def __str__(self): return 'texto'

@dataclass
class NullValue(Value):
  def __str__(self): return 'nulo'
