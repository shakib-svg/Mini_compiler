class LPProblem:
    def __init__(self, objective, constraints):
        self.objective = objective
        self.constraints = constraints

class Objective:
    def __init__(self, direction, expr):
        self.direction = direction.lower()  
        self.expr = expr

class Constraint:
    def __init__(self, left_expr, relop, right_expr):
        self.left_expr = left_expr
        self.relop = relop
        self.right_expr = right_expr

class Expr:
    pass

class BinOp(Expr):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(Expr):
    def __init__(self, value):
        self.value = value

class Var(Expr):
    def __init__(self, name):
        self.name = name
