class World:
  def __init__(self):
    self.next_id = 0

    self.types = {} # entity id -> Type
    self.values = {} # entity id -> Value
    self.const = set() # (entity id)[]

  # ---------------- CREATE VARIABLE ----------------
  def create(self, type_, value, is_const=False):
    var_id = self.next_id
    self.next_id += 1
    self.types[var_id] = type_
    self.values[var_id] = value

    if is_const:
      self.const.add(var_id)

    return var_id

  # ---------------- GETTERS ----------------
  def get_type(self, var_id):
    return self.types[var_id]

  def get_value(self, var_id):
    return self.values[var_id]

  def set_value(self, var_id, value):
    if var_id in self.const:
      raise Exception('Cannot modify const variable')

    self.values[var_id] = value

  def is_const(self, var_id):
    return var_id in self.const
