from lark import Lark,Transformer

class MyData(Transformer):
  def ID(self,token):
    return str(token)

  def arg_list(self,children):
    children

  def statement(self,children):
    return children[0]

  def calculation(self,children):
    left=int(children[0])
    op=children[1]
    right=int(children[2])

    ops={
      '+':lambda a,b:a+b,
      '-':lambda a,b:a-b,
      '*':lambda a,b:a*b,
      '/':lambda a,b:a/b,
    }

    return ops[op](left, right)

  def func(self, children):
    func_name=children[0]
    args=children[1]
    body=children[2:] 
    return f"Defined function {func_name} with args {args}"

  def start(self,children):
    return children

with open('./grammar.lark','r') as f:
  parser=Lark(f.read())

  text='5+3; 3+10; func f(x){3*5;}'
  tree=parser.parse(text)
  print(tree.pretty())

  result=MyData().transform(tree)
  print(result)
