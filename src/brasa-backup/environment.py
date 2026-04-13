class Environment:
  def __init__(self,parent=None):
    self.parent=parent

    self.variables={}
    self.types={}

  def define(
    self,
    name:str,
    var_type:str,
    value:any
  ):
    if name in self.variables:
      raise RuntimeError(f'Error: Variable "{name}" has already been declared.')

    self.types[name]=var_type
    self.variables[name]=value

  def get(self,name:str):
    if name not in self.variables:
      raise RuntimeError(f'Error: Variable "{name}" has not been declared.')
    
    return self.variables[name]

  def update(
    self,
    name:str,
    value:any
  ):
    if name not in self.variables:
      raise RuntimeError(f'Error: Variable "{name}" has not been declared.')

    self.variables[name]=value
