class Environment:
  def __init__(self,parent=None):
    self.values={}
    self.parent=parent

  def define(self,name,value):
    self.values[name]=value

  def get(self, name):
    if name in self.values:
      return self.values[name]
    if self.parent:
      return self.parent.get(name)

    raise NameError(f"Undefined variable '{name}'")
