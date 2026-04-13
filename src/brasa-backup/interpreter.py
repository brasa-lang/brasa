from brasa.core.scope import Scope

class BrasaInterpreter:
  def __init__(self):
    self.current_env=Scope()

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

  def visit_ProgramNode(self,node):
    for statement in node.statements:
      self.visit(statement)

  def visit_LiteralNode(self,node):
      return node.value

  def visit_VarLookupNode(self,node):
    return self.current_env.get(node.name)
  
  def visit_IncrementNode(self,node):
    current_val=self.current_env.get(node.name)

    self.current_env.update(
      node.name,
      current_val+1
    )

  def visit_DecrementNode(self,node):
    current_val=self.current_env.get(node.name)

    self.current_env.update(
      node.name,
      current_val-1
    )

  def visit_BinOpNode(self,node):
    left=self.visit(node.left)
    right=self.visit(node.right)
    
    ops={
        '+':lambda a,b:a+b,
        '-':lambda a,b:a-b,
        '*':lambda a,b:a*b,
        '/':lambda a,b:a/b,
        '==':lambda a,b:a==b,
        '!=':lambda a,b:a!=b,
        '>':lambda a,b:a>b,
        '<':lambda a,b:a<b,
        '>=':lambda a,b:a>=b,
        '<=':lambda a,b:a<=b,
    }

    return ops[node.op](left,right)

  def visit_DeclarationNode(self,node):
    initial_value=self.visit(node.value)
    self.current_env.define(
      node.name,
      node.var_type,
      initial_value
    )

  def visit_AssignmentNode(self,node):
    new_value=self.visit(node.value)
    self.current_env.update(node.name,new_value)

  def visit_PrintNode(self,node):
    result=self.visit(node.value)

    if result is True:
        print('verdadeiro')
    elif result is False:
        print('falso')
    else:
        print(result)

  def visit_IfNode(self,node):
    if self.visit(node.condition):
      previous_env=self.current_env
      self.current_env=Scope(parent=previous_env)

      try:
        for stmt in node.then_block:
          self.visit(stmt)
      finally:
        self.current_env=previous_env
    elif node.else_block:
      for stmt in node.else_block:
        self.visit(stmt)

  def visit_WhileNode(self, node):
    while self.visit(node.condition):
        for stmt in node.block:
            self.visit(stmt)

  def visit_UnaryMinusNode(self, node):
    value=self.visit(node.expr)
    
    if not isinstance(value, (int, float)):
      raise RuntimeError('Error: Unary operator "-" can only be used with numbers')
        
    return -value
