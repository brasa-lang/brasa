import sys

from pprint import pprint
from pathlib import Path

from lark import Lark

from src.core.ast_builder import ASTBuilder
from src.core.interpreter import Interpreter

def run_brasa():
  if len(sys.argv)<2:
    print('Use: python main.py <filename.brasa>')
    return

  file_path=Path(sys.argv[1])

  if not file_path.exists():
      print(f'Error: File "{file_path}" does not exist.')
      return

  grammar_path=Path(__file__).parent/'src'/'core'/'grammar.lark'

  with open(grammar_path, 'r', encoding='utf-8') as g:
    parser=Lark(
      g.read(),
      start='start',
      maybe_placeholders=True
    )

  with open(file_path, 'r', encoding='utf-8') as f:
    code=f.read()

  raw_tree=parser.parse(code)

  # pprint(raw_tree)

  transformer=ASTBuilder()
  ast=transformer.transform(raw_tree)

  # pprint(ast)

  interpreter=Interpreter()
  interpreter.visit(ast)

if __name__=='__main__':
  run_brasa()
