from lark import Transformer

from environment import Environment

ops={
  '+':lambda a,b:a+b,
  '-':lambda a,b:a-b,
  '*':lambda a,b:a*b,
  '/':lambda a,b:a/b,
}

class Interpreter(Transformer):
  def __init__(self):
    self.current_env=Environment()

  def number(self,tokens):
    return int(tokens[0])

  def var_lookup(self,tokens):
    var_name=str(tokens[0])
    return self.current_env.get(var_name)

  def assignment(self,children):
    var_name=str(children[0])
    value=children[1]
    self.current_env.define(var_name,value)

    return None

  def calculation(self, children):
    left,op,right=children
    return ops[op](left,right)

  def diga_statement(self,children):
    value=children[0]
    print(value)
    return value

  def start(self,children):
    return children
