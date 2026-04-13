class Symbol:
  def __init__(
    self,name,
    type_name,
    initial_value=None,
    is_const=False,
    is_nullable=False
  ):
    self.name=name
    self.type_name=type_name

    self.value=initial_value
    self.is_const=is_const
    self.is_nullable=is_nullable
