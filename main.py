import sys

from pprint import pprint
from pathlib import Path

from lark import Lark

from src.brasa.core.transformer import BrasaTransformer
from src.brasa.core.interpreter import BrasaInterpreter

def run_brasa():
  if len(sys.argv)<2:
    print('Use: python main.py <filename.brasa>')
    return

  file_path=Path(sys.argv[1])

  if not file_path.exists():
      print(f'Error: File "{file_path}" does not exist.')
      return

  grammar_path=Path(__file__).parent/'src'/'brasa'/'core'/'grammar.lark'

  with open(grammar_path, 'r', encoding='utf-8') as g:
    brasa_parser=Lark(g.read(),start='start')

  with open(file_path, 'r', encoding='utf-8') as f:
    code=f.read()

  raw_tree=brasa_parser.parse(code)

  # pprint(raw_tree)

  transformer=BrasaTransformer()
  ast=transformer.transform(raw_tree)

  # pprint(ast)
  
  interpreter=BrasaInterpreter()
  interpreter.visit(ast)

if __name__=='__main__':
  run_brasa()
