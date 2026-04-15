class LValue:
  def get(self,interpreter):
    raise NotImplementedError

  def set(self,interpreter,value):
    raise NotImplementedError

class VarLValue(LValue):
  def __init__(self,name):
    self.name = name

  def get(self,interpreter):
    var_id = interpreter.current_scope.lookup(self.name)
    return interpreter.world.get_value(var_id)

  def set(self,interpreter,value):
    var_id = interpreter.current_scope.lookup(self.name)
    interpreter.world.set_value(var_id,value)

class IndexLValue(LValue):
  def __init__(self,base,index_expr):
    self.base=base
    self.index_expr=index_expr

  def get(self,interpreter):
    arr=self.base.get(interpreter)
    index=interpreter.visit(self.index_expr)
    return arr[index]

  def set(self,interpreter,value):
    arr=self.base.get(interpreter)
    index=interpreter.visit(self.index_expr)
    arr[index]=value
