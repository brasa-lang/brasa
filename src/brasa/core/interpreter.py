from src.brasa.typing.scope import Scope

class BrasaInterpreter:
  def __init__(self):
    self.current_env=Scope()

  def visit(self,node):
    method_name=f'visit_{type(node).__name__}'
    visitor=getattr(
      self,
      method_name,
      self.generic_visit
    )

    return visitor(node)

  def generic_visit(self, node):
    raise Exception(f'Method visit_{type(node).__name__} does not exist.')

  def visit_ProgramNode(self,node):
    for statement in node.statements:
      self.visit(statement)

  def visit_LiteralNode(self,node):
    return node.value

  def visit_VarDeclarationNode(self,node):
    if node.initial_value is not None:
      initial_value=self.visit(node.initial_value)
    else:
      initial_value=None

    self.current_env.declare(
      name=node.name,
      type_name=node.type_name,
      initial_value=initial_value,
      is_const=node.is_const,
      is_nullable=node.is_nullable
    )

  def visit_UpdateVarNode(self, node):
    new_value = self.visit(node.expression)
    self.current_env.assign(node.name,new_value)

  def visit_PrintNode(self,node):
    result=self.visit(node.expression)

    if result is True:
      print('verdadeiro')
    elif result is False:
      print('falso')
    elif result is None:
      print('nulo')
    else:
      print(result)

  def visit_IdentifierNode(self, node):
    return self.current_env.lookup(node.name)
