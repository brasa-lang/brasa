from dataclasses import dataclass

@dataclass
class ModuleType: pass

@dataclass
class ModuleValue:
  name:str
  exports:list[any]

@dataclass
class Member:
  obj:any
  name:str

@dataclass
class ImportStatement:
  path:str
  alias:str

@dataclass
class ExportStatement:
  items:list[any]

@dataclass
class ExportItem:
  name:str
  alias:str
