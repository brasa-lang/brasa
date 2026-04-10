from lark import Lark

from interpreter import Interpreter

with open('./grammar.lark','r') as f:
  parser=Lark(f.read())

  with open('./test.brasa','r') as f:
    tree=parser.parse(f.read())
    print(tree.pretty())

    result=Interpreter().transform(tree)
    print(result)
