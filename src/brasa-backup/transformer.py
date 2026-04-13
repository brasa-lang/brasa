from lark import Transformer
from brasa.core.nodes import *

class BrasaTransformer(Transformer):
  # Literals
  def integer(self,children):
    return LiteralNode(int(children[0]))

  def decimal(self,children):
    return LiteralNode(float(children[0]))

  def string(self,children):
    normalized_string=children[0][1:-1]
    return LiteralNode(normalized_string)

  def true_val(self,_):
    return LiteralNode(True)

  def false_val(self,_):
    return LiteralNode(False)

  # Expressions
  def product(self,children):
    return self._build_binop(children)

  def sum(self,children):
    return self._build_binop(children)

  def comparison(self,children):
    return self._build_binop(children)

  def _build_binop(self, children):
    if len(children) == 1:
      return children[0]

    left=children[0]
    op=str(children[1])
    right=children[2]
    return BinOpNode(left,op,right)

  def increment(self, children):
    return IncrementNode(str(children[0]))

  def decrement(self, children):
    return DecrementNode(str(children[0]))
  
  def unary_minus(self, children):
    return UnaryMinusNode(children[0])

  # Variables
  def declaration(self, children):
    var_type=str(children[0])
    name=str(children[1])
    value=children[2]
    return DeclarationNode(var_type,name,value)

  def update_var(self, children):
    name=str(children[0])
    value=children[1]
    return AssignmentNode(name,value)

  def var_lookup(self,children):
    return VarLookupNode(str(children[0]))
  
  # Turing
  def block(self,children):
    return children

  def if_statement(self, children):
    condition=children[0]
    then_block=children[1]
    else_block=children[2] if len(children) > 2 else None

    return IfNode(
      condition,
      then_block,
      else_block
    )

  def while_statement(self, children):
    return WhileNode(
      children[0],
      children[1]
    )

  # REMOVE LATER
  def diga_statement(self,children):
    return PrintNode(children[0])

  # int main(){}
  def start(self,children):
    return ProgramNode(children)
