import click
import sys

from brasa.runner import run_file
from brasa.repl import repl

def main():
  if len(sys.argv) > 1:
    run_file(sys.argv[1])
  else:
    repl()

if __name__=='__main__':
  main()
