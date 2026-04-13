from src.symbols.scope import Scope
from src.symbols.world import World

class Interpreter:
  def __init__(self):
    self.current_env=Scope()
    self.world=World()

  def visit(self,node):
    method_name=f'visit_{type(node).__name__}'
    visitor=getattr(
      self,
      method_name,
      self.generic_visit
    )

    return visitor(node)

  def generic_visit(self, node):
    raise Exception(f'Method visit_{type(node).__name__} does not exist.')

  def visit_ProgramNode(self,node):
    for statement in node.statements:
      self.visit(statement)
