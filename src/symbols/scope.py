class Scope:
  def __init__(self, parent=None):
    self.parent = parent
    self.symbols = {} # variable name -> entity id

  # ---------------- DECLARE ----------------
  def declare(self, name, var_id):
    if name in self.symbols:
      raise Exception(f'Error: Variable "{name}" has already been declared in this scope')

    self.symbols[name] = var_id

  # ---------------- LOOKUP ----------------
  def lookup(self, name):
    if name in self.symbols:
      return self.symbols[name]

    if self.parent:
      return self.parent.lookup(name)

    raise Exception(f'Variable "{name}" has not been found')
