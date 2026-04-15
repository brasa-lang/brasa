from brasa.core.types.operators import BinaryOperationEnum

class VariablesMixin:
  def visit_Identifier(self,node):
    var_id=self.current_scope.lookup(node.name)

    return self.world.get_value(var_id)

  def visit_VariableDeclarationStatement(self,node):
    value=self.visit(node.expr) if node.expr is not None else None

    var_id=self.world.create(
      type=node.type,
      value=value,
      is_const=node.is_const
    )

    self.current_scope.declare(
      name=node.id.name,
      entity_id=var_id
    )

  def visit_AssignmentStatement(self,node):
    value=self.visit(node.expr)
    node.target.set(self,value)

  def visit_CompoundAssignmentStatement(self, node):
    current=node.target.get(self)
    value=self.visit(node.expr)

    if node.op==BinaryOperationEnum.ADDITION:
      result=current+value
    elif node.op==BinaryOperationEnum.SUBTRACTION:
      result=current-value
    elif node.op==BinaryOperationEnum.MULTIPLICATION:
      result= current*value
    elif node.op==BinaryOperationEnum.DIVISION:
      result=current/value

    node.target.set(self,result)

  def visit_PostfixStatement(self,node):
    current=node.target.get(self)

    if node.op==BinaryOperationEnum.ADDITION:
      new_value=current+1
    else:
      new_value=current-1

    node.target.set(self,new_value)
