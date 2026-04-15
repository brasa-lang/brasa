from lark import Transformer

from brasa.parser.mixins.basics_mixin import BasicsMixin

from brasa.parser.mixins.variables_mixin import VariablesMixin
from brasa.parser.mixins.primitive_types_mixin import PrimitiveTypesMixin
from brasa.parser.mixins.primitive_values_mixin import PrimitiveValuesMixin

from brasa.parser.mixins.operators_mixin import OperatorsMixin

from brasa.parser.mixins.flow_mixin import FlowMixin

from brasa.parser.mixins.arrays_mixin import ArrayMixin
from brasa.parser.mixins.functions_mixin import FunctionsMixin

class ASTBuilder(
  Transformer,

  BasicsMixin,

  VariablesMixin,
  PrimitiveTypesMixin,
  PrimitiveValuesMixin,

  OperatorsMixin,

  FlowMixin,

  ArrayMixin,
  FunctionsMixin,
):
  pass
