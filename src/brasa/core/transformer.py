from src.brasa.core.nodes import *

from lark import Transformer, Token
from src.brasa.typing.tokens import INTEGER,REAL,STRING,BOOLEAN

class BrasaTransformer(Transformer):
  # Literals
  def INTEGER(self, t): return LiteralNode(int(t))
  def REAL(self, t):    return LiteralNode(float(t))
  def STRING(self, t):  return LiteralNode(str(t[1:-1]))
  def BOOLEAN(self, t): return LiteralNode(t == "verdadeiro")
  def NULL(self, t):    return LiteralNode(None)

  def expression(self, children): return children[0]
  def statement(self, children):  return children[0]
  def top_item(self, children):   return children[0]

  # Statements
  def var_declaration(self, children):
    is_const=any(isinstance(c,Token) and c.type=='CONST' for c in children)
    is_nullable=any(isinstance(c,Token) and c.type=='NULLABLE' for c in children)

    type_token=next(c for c in children if isinstance(c,Token) and c.type=='PRIMITIVE_TYPE')
    name_node = next(c for c in children if isinstance(c, IdentifierNode))
    
    value=None
    if any(isinstance(c,Token) and c.type=='ASSIGN' for c in children):
      value=children[-1]

    return VarDeclarationNode(
      name=str(name_node.name),
      type_name=str(type_token),
      initial_value=value,
      is_const=is_const,
      is_nullable=is_nullable,
    )

  def update_var(self, children):
    return UpdateVarNode(name=children[0].name, expression=children[1])

  def ID(self, t):
    return IdentifierNode(name=str(t))

  def diga_statement(self, children):
    return PrintNode(expression=children[0])

  def start(self, children):
      return ProgramNode(statements=children)
  