from lark import v_args

from brasa.core.nodes.modules import ImportStatement,ExportItem,ExportStatement,Member

class ModulesMixin:
  @v_args(inline=True)
  def import_statement(
    self,
    path,
    alias=None
  ):
    return ImportStatement(
      path=path,
      alias=alias.name if alias else None
    )

  def module_path(
    self,
    parts
  ):
    return [p.name for p in parts]

  @v_args(inline=True)
  def export_statement(
    self,
    items
  ):
    return ExportStatement(items)

  @v_args(inline=True)
  def export_item(
    self,
    name,
    alias
  ):
    return ExportItem(
      name=name.name,
      alias=alias.name if alias is not None else None
    )

  def export_list(
    self,
    items
  ):
    return items

  @v_args(inline=True)
  def member(
    self,
    obj,
    name
  ):
    return Member(
      obj=obj,
      name=name
    )