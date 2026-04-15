from dataclasses import dataclass

@dataclass
class Program:
  statements:list[any]

@dataclass
class Identifier:
  name:str

@dataclass
class Block:
  statements:any

@dataclass
class PrintStatement:
  expr:any
