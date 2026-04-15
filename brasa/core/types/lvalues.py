from dataclasses import dataclass

class LValue:
  def get(self,interpreter):
    raise NotImplementedError

  def set(self,interpreter,value):
    raise NotImplementedError

@dataclass
class VarLValue(LValue):
  name:str

  def get(self,interpreter):
    entity_id=interpreter.current_scope.lookup(self.name)

    return interpreter.world.get_value(entity_id)

  def set(
    self,
    interpreter,
    value
  ):
    entity_id=interpreter.current_scope.lookup(self.name)
    interpreter.world.set_value(
      entity_id,
      value
    )

@dataclass
class IndexLValue(LValue):
  base:any
  index:any

  def get(self,interpreter):
    arr=self.base.get(interpreter)
    index=interpreter.visit(self.index)

    return arr[index]

  def set(
    self,
    interpreter,
    value
  ):
    arr=self.base.get(interpreter)
    index=interpreter.visit(self.index)

    arr[index]=value
