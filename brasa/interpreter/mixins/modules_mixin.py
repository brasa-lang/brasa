from pathlib import Path

from brasa.core.runtime.scope import Scope
from brasa.core.runtime.world import World
from brasa.core.nodes.modules import ModuleValue,ModuleType

from brasa.parser.ast_builder import ASTBuilder

class ModulesMixin:
  def execute_local_module():
    pass

  def execute_system_module():
    pass

  def execute_module(self, path_parts):
    file_path=Path(self.base_path).joinpath(*path_parts).with_suffix('.brasa')

    if not file_path.exists():
      raise Exception(f'Module not found: {'.'.join(path_parts)}')

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
      name='.'.join(path_parts),
      exports=self._current_exports
    )

    self.current_scope=old_scope
    self._current_exports=old_exports
    self.world=old_world

    return module

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
