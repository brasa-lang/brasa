class Scope:
  def __init__(self,parent=None):
    self.parent=parent
    self.symbols={} # Variable Name -> Entity Id

  def declare(
    self,
    name,
    entity_id
  ):
    if name in self.symbols:
      raise Exception(f'Error: Variable "{name}" has already been declared in this scope')

    self.symbols[name]=entity_id

  def lookup(self,name):
    if name in self.symbols:
      return self.symbols[name]

    if self.parent:
      return self.parent.lookup(name)

    raise Exception(f'Variable "{name}" has not been found')
