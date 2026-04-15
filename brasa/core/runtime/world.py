class World:
  def __init__(self):
    self.next_id=0

    self.types={} # Entity Id -> Type
    self.values={} # Entity Id -> Value
    self.const=set() # (Entity Id)[]

  def create(
    self,
    type,
    value,
    is_const=False
  ):
    entity_id=self.next_id
    self.next_id+=1

    self.types[entity_id]=type
    self.values[entity_id]=value

    if is_const:
      self.const.add(entity_id)

    return entity_id

  def get_type(self,entity_id):
    return self.types[entity_id]

  def get_value(self,entity_id):
    return self.values[entity_id]

  def set_value(
    self,
    entity_id,
    value
  ):
    if entity_id in self.const:
      raise Exception('Cannot modify const variable')

    self.values[entity_id]=value

  def is_const(self,entity_id):
    return entity_id in self.const
