from lark import Lark,Transformer

class MyData(Transformer):
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

  def start(self,children):
    return children

with open('./grammar.lark','r') as f:
  parser=Lark(f.read())

  text='5+3'
  tree=parser.parse(text)
  print(tree.pretty())

  result=MyData().transform(tree)
  print(result)
