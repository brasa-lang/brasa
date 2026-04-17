from pathlib import Path
import importlib.util

from brasa.core.runtime.scope import Scope
from brasa.core.runtime.world import World
from brasa.core.nodes.modules import ModuleValue,ModuleType
from brasa.core.nodes.functions import FunctionType,BuiltinFunction

from brasa.parser.ast_builder import ASTBuilder

class ModulesMixin:
  def execute_local_module():
    pass

  def execute_system_module():
    pass

  def execute_module(self, path_parts):
    module_name='.'.join(path_parts)
    file_path=Path(self.base_path).joinpath(*path_parts).with_suffix('.brasa')

    if file_path.exists():
      code=file_path.read_text(encoding='utf-8')
      raw_tree=self.parser.parse(code)
      ast=ASTBuilder().transform(raw_tree)

      old_scope=self.current_scope
      old_exports=self._current_exports
      old_world=self.world

      self.current_scope=Scope()
      self.world=World()
      self._current_exports={}

      for stmt in ast.statements:
        self.visit(stmt)

      module=ModuleValue(
        name=module_name,
        exports=self._current_exports
      )

      self.current_scope=old_scope
      self._current_exports=old_exports
      self.world=old_world

      return module
    else:
      std_file = self.std_path.joinpath(*path_parts).with_suffix(".py")

      if std_file.exists():
          spec = importlib.util.spec_from_file_location(module_name, std_file)
          mod = importlib.util.module_from_spec(spec)
          spec.loader.exec_module(mod)

          if not hasattr(mod, "exports"):
              raise Exception(f"Builtin module '{module_name}' must define 'exports'")

          exports = {}

          for name, value in mod.exports.items():
              value=BuiltinFunction(
                name=None,
                func=value,
              )
              entity_id = self.world.create(
                  type=FunctionType(
                    param_types=[],
                    return_type=None
                  ),
                  value=value
              )

              exports[name] = value

          return ModuleValue(
              name=module_name,
              exports=exports
          )

      raise Exception(f'Module not found: {'.'.join(path_parts)}')

  def visit_ImportStatement(self,node):
    module=self.execute_module(node.path)
    alias=node.alias or node.path[-1]

    entity_id=self.world.create(
      type=ModuleType(),
      value=module
    )

    self.current_scope.declare(alias,entity_id)

  def visit_ExportStatement(self,node):
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
