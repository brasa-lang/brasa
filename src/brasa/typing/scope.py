from math import trunc

from src.brasa.typing.symbol import Symbol
from src.brasa.typing.tokens import STRING,INTEGER,REAL,BOOLEAN

DEFAULT_VALUES={
  INTEGER:0,
  REAL:0.0,
  BOOLEAN:False,
  STRING:""
}

class Scope:
  def __init__(self,parent=None):
    self.parent=parent
    self.symbols={}

  # Declare variable
  def declare(
    self,
    name,
    type_name,
    initial_value,
    is_const,
    is_nullable
  ):
    # Variable has already been declared
    if name in self.symbols:
      raise Exception(f'Erro: Variável "{name}" já declarada.')

    effective_value=initial_value

    if initial_value is None:
      # Const must have an initial value const int x; or const int x := nulo;
      if is_const:
        raise Exception(f'Erro: Variável "{name}" foi declarada como constante, mas não teve nenhum valor inicial atribuido.')

      if is_nullable:
        # int x;
        effective_value=None
      else:
        # int x;
        # Silently assign a default value
        effective_value=DEFAULT_VALUES.get(type_name)
    else:
      effective_value=initial_value

    if not is_nullable:
      self.type_checking(effective_value,type_name)

    self.symbols[name]=Symbol(
      name,
      type_name,
      effective_value,
      is_const,
      is_nullable,
    )

  # Get value of variable
  def lookup(self, name):
    if name in self.symbols:
      return self.symbols[name].value

    if self.parent is not None:
      return self.parent.lookup(name)

    raise Exception(f'Erro: Variável "{name}" não foi declarada.')

  # Assign a new value to a variable
  def assign(
    self,
    name,
    value
  ):
    if name in self.symbols:
      symbol = self.symbols[name]

      if symbol.is_const:
        raise Exception(f'Erro: Variável "{name}" é constante e não pode ser reatribuída.')

      if not symbol.is_nullable and value is None:
        raise Exception(f'Erro: Não é possível atribuir um valor nulo a um variável que não pode receber nulo')

      if symbol.is_nullable:
        symbol.value=value
        return

      validated_value=self.type_checking(
        value,
        symbol.type_name
      )

      symbol.value=validated_value

      return

    if self.parent:
      return self.parent.assign(name, value)

    raise Exception(f'Erro: Variável "{name}" não foi declarada.')

  def type_checking(
    self,
    value,
    type_name
  ):
    # Declaring variable of type texto
    if type_name==STRING:
      if not isinstance(value,str):
        raise Exception(f'Error: Tentativa de atribuir a uma variável do tipo texto um valor que não é texto.')
      return value

    # Declaring variable of type inteiro
    if type_name==INTEGER:
      if isinstance(value,bool) or not isinstance(value,(int,float)):
        raise Exception(f'Erro: Tentativa de atribuir a uma variável do tipo inteiro um valor que não é compatível com inteiro')
      return trunc(value)

    # Declaring variable of type real
    if type_name==REAL:
      if isinstance(value,bool) or not isinstance(value,(int,float)):
        raise Exception(f'Erro: Tentativa de atribuir a uma variável do tipo real um valor que não é compatível com real')
      return float(value)

    # Declaring variable of type booleano
    if type_name==BOOLEAN:
      if not isinstance(value,bool):
        raise Exception(f'Error: Tentativa de atribuir a uma variável do tipo lógico um valor que não é lógico.')
      return value

    return value
