class Scope:
  def __init__(self,parent=None):
    self.parent=parent # points to the parent scope, if any. If None, this is the global scope.

    self.symbols={} # str (name of the variable) -> int (id of the variable in the world)

  # const numero x := 5;
  def declare(
    self,
    name,
    type_name,
    initial_value=None,
    is_const=False,
  ):
    pass

  # numero x := 20;
  def assign(self,name,value):
    pass

  # x
  def lookup(self,name):
    pass
