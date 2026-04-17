from pathlib import Path

from brasa.core.runtime.scope import Scope
from brasa.core.runtime.world import World

from brasa.interpreter.mixins.basics_mixin import BasicsMixin

from brasa.interpreter.mixins.variables_mixin import VariablesMixin
from brasa.interpreter.mixins.primitive_values_mixin import PrimitiveValuesMixin

from brasa.interpreter.mixins.operators_mixin import OperatorsMixin

from brasa.interpreter.mixins.flow_mixin import FlowMixin

from brasa.interpreter.mixins.arrays_mixin import ArrayMixins
from brasa.interpreter.mixins.functions_mixin import FunctionsMixin

from brasa.interpreter.mixins.modules_mixin import ModulesMixin

class Interpreter(
  BasicsMixin,

  VariablesMixin,
  PrimitiveValuesMixin,
  OperatorsMixin,

  FlowMixin,

  ArrayMixins,
  FunctionsMixin,

  ModulesMixin
):
  def __init__(self,entry_file,root,parser):
    self.current_scope=Scope()
    self.world=World()
    self.parser=parser

    if root:
      self.base_path = Path(root).resolve()
    elif entry_file:
      self.base_path = Path(entry_file).resolve().parent
    else:
      self.base_path = Path.cwd()

    self.std_path = (
        Path(__file__)
          .resolve()
          .parent
          .parent
    )

    self._current_exports = None

  def visit(self,node):
    method_name=f'visit_{type(node).__name__}'
    visitor=getattr(
      self,
      method_name,
      self.generic_visit
    )

    return visitor(node)

  def generic_visit(self, node):
    raise Exception(f'Method visit_{type(node).__name__} does not exist.')
