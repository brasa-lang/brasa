from brasa.runner import Interpreter
from brasa.runner import run_code

import readline

readline.read_history_file('.brasa_history')
readline.write_history_file('.brasa_history')

def repl():
  interpreter=Interpreter()
  buffer=''

  while True:
    try:
      prompt='>>> ' if not buffer else '... '
      line=input(prompt)

      if line.strip() in {'exit','quit'}:
        break

      buffer+=line+'\n'

      try:
        result=run_code(
          buffer,
          interpreter=interpreter
        )

        buffer=''

        if result is not None:
          print(result)
      except Exception:
        continue
    except KeyboardInterrupt:
      print('\nKeyboardInterrupt')
      buffer=''
