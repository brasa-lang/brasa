from src.symbols.scope import Scope
from src.symbols.world import World

from src.core.utils.operators import BinOp

class Interpreter:
  # ---------------- PROGRAM ----------------

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

  def visit_Program(self,node):
    for statement in node.statements:
      self.visit(statement)

  # ---------------- VARIABLES ----------------

  def visit_Identifier(self, node):
    var_id = self.current_scope.lookup(node.name)
    return self.world.get_value(var_id)

  def visit_VarDeclarationStatement(self,node):
    value = self.visit(node.expr) if node.expr is not None else None

    var_id=self.world.create(
      type_=node.type,
      value=value,
      is_const=node.is_const
    )

    self.current_scope.declare(node.id.name,var_id)

  def visit_UpdateVariableStatement(self,node):
    var_id = self.current_scope.lookup(node.id.name)

    if self.world.is_const(var_id):
      raise Exception(f"Cannot assign to const '{node.id.name}'")

    value = self.visit(node.expr)
    self.world.set_value(var_id, value)

  # ---------------- LITERALS ----------------

  def visit_IntegerLiteral(self, node):
    return node.value

  def visit_FloatLiteral(self, node):
    return node.value

  def visit_NullLiteral(self, node):
    return None

  def visit_ArrayLiteral(self, node):
    return [self.visit(elem) for elem in node.elements]

  def visit_BinaryOp(self, node):
    left = self.visit(node.left)
    right = self.visit(node.right)

    op = node.op

    if op == BinOp.ADD:
      return left + right
    if op == BinOp.SUB:
      return left - right
    if op == BinOp.MUL:
      return left * right
    if op == BinOp.DIV:
      return left / right

    if op == BinOp.GT:
      return left > right
    if op == BinOp.LT:
      return left < right
    if op == BinOp.GE:
      return left >= right
    if op == BinOp.LE:
      return left <= right
    if op == BinOp.EQ:
      return left == right
    if op == BinOp.NE:
      return left != right

    if op == BinOp.AND:
      return left and right
    if op == BinOp.OR:
      return left or right

    raise Exception(f"Unknown operator: {op}")

  # ---------------- STATEMENTS ----------------

  def visit_PrintStatement(self, node):
    value = self.visit(node.expr)

    if value is None:
      print('nulo')
    else:
      print(value)
