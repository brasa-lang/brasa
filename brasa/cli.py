import click
from importlib import metadata
import sys

from brasa.runner import run_file
from brasa.repl import repl

__version__=metadata.version('brasa-lang')

@click.command()
@click.argument(
  'filename',
  required=False,
  type=click.Path(exists=True)
)
@click.version_option(
  version=__version__,
  prog_name='Brasa'
)
def main(filename):
  """
    Brasa Programming Language CLI.

    If FILENAME is provided, executes the script.
    Otherwise, starts the interactive REPL.
  """

  if filename is not None:
    try: run_file(filename)
    except Exception: sys.exit(1)
  else:
    repl()

if __name__=='__main__':
  main()
