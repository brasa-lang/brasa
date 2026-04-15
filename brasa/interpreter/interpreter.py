from brasa.runtime.scope import Scope
from brasa.runtime.world import World

from brasa.core.nodes.values import FunctionValue
from brasa.core.types.operators import BinaryOperationEnum,UnaryOperationEnum

from brasa.interpreter.signals import BreakSignal,ContinueSignal,ReturnSignal

class Interpreter:
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

  # ---------------- BASICS ----------------

  def visit_Program(self,node):
    for statement in node.statements:
      self.visit(statement)

  def visit_Block(self, node):
    old_scope = self.current_scope
    self.current_scope = Scope(parent=old_scope)

    for stmt in node.statements:
      self.visit(stmt)

    self.current_scope = old_scope

  # ---------------- VARIABLES ----------------

  def visit_Identifier(self, node):
    var_id = self.current_scope.lookup(node.name)
    return self.world.get_value(var_id)

  def visit_VariableDeclarationStatement(self,node):
    value = self.visit(node.expr) if node.expr is not None else None

    var_id=self.world.create(
      type_=node.type,
      value=value,
      is_const=node.is_const
    )

    self.current_scope.declare(node.id.name,var_id)

  def visit_AssignmentStatement(self,node):
    var_id = self.current_scope.lookup(node.id.name)

    if self.world.is_const(var_id):
      raise Exception(f"Cannot assign to const '{node.id.name}'")

    value = self.visit(node.expr)
    self.world.set_value(var_id, value)

  def visit_CompoundAssignmentStatement(self, node):
    var_id = self.current_scope.lookup(node.id.name)
    current=self.world.get_value(var_id)
    value = self.visit(node.expr)

    if node.op == BinaryOperationEnum.ADD:
      result = current + value
    elif node.op == BinaryOperationEnum.SUB:
      result = current - value
    elif node.op == BinaryOperationEnum.MUL:
      result = current * value
    elif node.op == BinaryOperationEnum.DIV:
      result = current / value

    self.world.set_value(var_id,result)

  def visit_PostfixStatement(self, node):
    var_id = self.current_scope.lookup(node.id.name)
    current=self.world.get_value(var_id)

    if node.op==BinaryOperationEnum.ADD:
      self.world.set_value(var_id,current+1)
    else:
      self.world.set_value(var_id,current-1)

  # ---------------- VALUES ----------------

  def visit_IntegerValue(self, node):
    return node.value

  def visit_FloatValue(self, node):
    return node.value

  def visit_StringLiteral(self, node):
    return node.value

  def visit_NullValue(self, node):
    return None

  def visit_BooleanValue(self, node):
    return node.value

  def visit_ArrayValue(self, node):
    return [self.visit(elem) for elem in node.elements]

  # ---------------- OPERATORS ----------------

  def visit_BinaryOp(self, node):
    op = node.op

    if op == BinaryOperationEnum.AND:
      left=self.visit(node.left)

      if not left:
        return False

      right=self.visit(node.right)
      return bool(right)

    if node.op == BinaryOperationEnum.OR:
      left = self.visit(node.left)

      if left:
        return True

      right = self.visit(node.right)
      return bool(right)

    left = self.visit(node.left)
    right = self.visit(node.right)

    if op == BinaryOperationEnum.ADD:
      return left + right
    if op == BinaryOperationEnum.SUB:
      return left - right
    if op == BinaryOperationEnum.MUL:
      return left * right
    if op == BinaryOperationEnum.DIV:
      return left / right

    if op == BinaryOperationEnum.GT:
      return left > right
    if op == BinaryOperationEnum.LT:
      return left < right
    if op == BinaryOperationEnum.GE:
      return left >= right
    if op == BinaryOperationEnum.LE:
      return left <= right
    if op == BinaryOperationEnum.EQ:
      return left == right
    if op == BinaryOperationEnum.NE:
      return left != right

    raise Exception(f"Unknown operator: {op}")

  def visit_UnaryOp(self, node):
    value = self.visit(node.expr)

    if node.op == UnaryOperationEnum.NEG:
      return -value

    if node.op == UnaryOperationEnum.NOT:
      return not value

    raise Exception(f"Unknown unary operator: {node.op}")

  # ---------------- CONTROL FLOW ----------------

  def visit_IfStatement(self, node):
    condition = self.visit(node.condition)

    if condition:
      return self.visit(node.then_block)

    if node.else_branch:
      return self.visit(node.else_branch)

  def visit_WhileStatement(self, node):
    while self.visit(node.condition):
      try:
        self.visit(node.body)

      except ContinueSignal:
        continue

      except BreakSignal:
        break

  def visit_BreakStatement(self, node):
    raise BreakSignal()

  def visit_ContinueStatement(self, node):
    raise ContinueSignal()

  # ---------------- FUNCTIONS ----------------

  def visit_FunctionDeclaration(self, node):
    func=FunctionValue(
      params=node.params,
      body=node.body,
      return_type=node.return_type,
      closure_scope=self.current_scope
    )

    var_id=self.world.create(
      type_=None,
      value=func,
      is_const=True
    )

    self.current_scope.declare(node.name.name, var_id)

  def visit_LambdaExpression(self, node):
    return FunctionValue(
      params=node.params,
      body=node.body,
      return_type=node.return_type,
      closure_scope=self.current_scope,
    )
  
  def visit_CallExpression(self, node):
    func=self.visit(node.callee)
    args=[self.visit(arg) for arg in node.args]

    new_scope=Scope(parent=func.closure_scope)

    for param, arg in zip(func.params, args):
      var_id = self.world.create(type_=param[0], value=arg)
      new_scope.declare(param[1].name, var_id)

    old_scope=self.current_scope
    self.current_scope=new_scope

    try:
      self.visit(func.body)
      result=None
    except ReturnSignal as r:
      result=r.value

    self.current_scope=old_scope

    return result

  def visit_ReturnStatement(self, node):
    value=None

    if node.expr:
      value=self.visit(node.expr)

    raise ReturnSignal(value)

  # ---------------- REMOVE LATER ----------------

  def visit_PrintStatement(self, node):
    value = self.visit(node.expr)

    if value is None:
      print('nulo')
    elif value is True:
      print('verdadeiro')
    elif value is False:
      print('falso')
    else:
      print(value)
