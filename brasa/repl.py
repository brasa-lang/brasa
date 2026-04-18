import click
from importlib import metadata

from brasa.runner import Interpreter
from brasa.runner import run_code

def repl(
  entry_file=None,
  root=None
):
  ascii_art=r'''
==========================================================
 _______    _______        __        ________     __      
|   _  "\  /"      \      /""\      /"       )   /""\     
(. |_)  :)|:        |    /    \    (:   \___/   /    \    
|:     \/ |_____/   )   /' /\  \    \___  \    /' /\  \   
(|  _  \\  //      /   //  __'  \    __/  \\  //  __'  \  
|: |_)  :)|:  __   \  /   /  \\  \  /" \   :)/   /  \\  \ 
(_______/ |__|  \___)(___/    \___)(_______/(___/    \___)

==========================================================
  '''

  click.secho(ascii_art,fg='yellow')

  __version__=metadata.version('brasa-lang')
  click.secho(f'Brasa, version {__version__}',fg='green')

  click.secho('Hi! This is Brasa Interactive Environment.',fg='green')
  click.secho('Type "exit" or "quit" or hit Ctrl+D to leave',fg='green')

  print()

  interpreter=Interpreter(
    entry_file=entry_file,
    root=root
  )
  buffer=''

  while True:
    try:
      if not buffer:
        prompt=click.style(
          '>>> ',
          fg='green',
          bold=True
        )
      else:
        prompt=click.style(
          '... ',
          fg='green',
        )

      line=input(prompt)

      if line.strip() in {'exit','quit'}:
        bye_message()
        break

      buffer+=line+'\n'

      try:
        result=run_code(
          buffer,
          interpreter=interpreter,
        )

        buffer=''

        if result is not None:
          print(result)
          print()
          buffer=''
      except Exception as e:
        pass
    except EOFError:
      bye_message()
      break
    except KeyboardInterrupt:
      click.secho('\nKeyboardInterrupt',fg='blue')
      print()
      buffer=''

def bye_message():
  print()
  click.secho('Exiting...',fg='blue')
  click.secho('It was nice talking to you (ꈍᴗꈍ)♡',fg='blue')
  print()
