from pathlib import Path
import importlib.util

from brasa.core.runtime.scope import Scope
from brasa.core.runtime.world import World
from brasa.core.nodes.modules import ModuleValue,ModuleType,ExportStatement,ImportStatement
from brasa.core.nodes.functions import FunctionType,BuiltinFunction

from brasa.parser.ast_builder import ASTBuilder

class ModulesMixin:
  def execute_local_module(
    self,
    module_name:str,
    file_path
  ):
    code=file_path.read_text(encoding='utf-8')
    raw_tree=self.parser.parse(code)
    ast=ASTBuilder().transform(raw_tree)

    old_scope=self.current_scope
    old_world=self.world

    self.current_scope=Scope()
    self.world=World()
    self._current_exports={}

    for statement in ast.statements: self.visit(statement)

    module=ModuleValue(
      name=module_name,
      exports=self._current_exports
    )

    self.current_scope=old_scope
    self.world=old_world

    return module

  def execute_system_module(
    self,
    module_name:str,
    std_file
  ):
    spec=importlib.util.spec_from_file_location(
      module_name,
      std_file
    )

    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module,'exports'):
      raise Exception(f'Python module "{module_name}" does not define "exports"')

    exports={}

    for name,value in module.exports.items():
      value=BuiltinFunction(
        name=None,
        func=value,
      )

      self.world.create(
        type=FunctionType(
          param_types=[],
          return_type=None
        ),
        value=value
      )

      exports[name]=value

    return ModuleValue(
      name=module_name,
      exports=exports
    )

  def execute_module(self, path_parts):
    module_name='.'.join(path_parts)
    file_path=Path(self.base_path).joinpath(*path_parts).with_suffix('.brasa')

    if file_path.exists():
      return self.execute_local_module(
        module_name=module_name,
        file_path=file_path
      )
    else:
      std_file=self.std_path.joinpath(*path_parts).with_suffix(".py")

      if std_file.exists():
        return self.execute_system_module(
          module_name=module_name,
          std_file=std_file
        )

      raise Exception(f'Module not found: {module_name}')

  def visit_ImportStatement(self,node:ImportStatement):
    module=self.execute_module(node.path)
    alias=node.alias or node.path[-1]

    entity_id=self.world.create(
      type=ModuleType(),
      value=module
    )

    self.current_scope.declare(alias,entity_id)

  def visit_ExportStatement(self,node:ExportStatement):
    if self._current_exports is None:
      raise Exception('export error')

    for item in node.items:
      name=item.name
      alias=item.alias or name

      entity_id=self.current_scope.lookup(name)
      value=self.world.get_value(entity_id)

      self._current_exports[alias]=value

  def visit_Member(self,node):
    obj=self.visit(node.obj)

    if node.name.name not in obj.exports:
      raise Exception(
        f'Module "{obj.name}" has no export "{node.name}"'
      )

    return obj.exports[node.name.name]
