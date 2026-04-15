from brasa.core.runtime.scope import Scope
from brasa.core.runtime.world import World

from brasa.interpreter.mixins.basics_mixin import BasicsMixin

from brasa.interpreter.mixins.variables_mixin import VariablesMixin
from brasa.interpreter.mixins.primitive_values_mixin import PrimitiveValuesMixin

from brasa.interpreter.mixins.operators_mixin import OperatorsMixin

from brasa.interpreter.mixins.flow_mixin import FlowMixin

from brasa.interpreter.mixins.arrays_mixin import ArrayMixins
from brasa.interpreter.mixins.functions_mixin import FunctionsMixin

class Interpreter(
  BasicsMixin,

  VariablesMixin,
  PrimitiveValuesMixin,
  OperatorsMixin,

  FlowMixin,

  ArrayMixins,
  FunctionsMixin
):
  def __init__(self):
    self.current_scope=Scope()
    self.world=World()

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
