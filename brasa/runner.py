from pathlib import Path

from lark import Lark

from brasa.parser.ast_builder import ASTBuilder
from brasa.interpreter.interpreter import Interpreter

def load_grammar(grammar_path):
  with open(
    grammar_path,
    'r',
    encoding='utf-8'
  ) as g:
    parser=Lark(
      g.read(),
      start='start',
      maybe_placeholders=True
    )

  return parser

def run_code(
  code:str,
  interpreter=None
):
  parser=load_grammar(
    Path(__file__).parent/'parser'/'grammar.lark'
  )

  raw_tree=parser.parse(code)
  ast=ASTBuilder().transform(raw_tree)

  if interpreter is None:
    interpreter = Interpreter()

  return interpreter.visit(ast)

def run_file(file_path:str):
  file_path=Path(file_path).resolve()

  if not file_path.exists():
    print(f'Error: File "{file_path}" does not exist.')
    return

  with open(file_path,'r') as f:
    code=f.read()

  run_code(code)
