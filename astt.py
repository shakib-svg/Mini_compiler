# ast.py

class LPProblem:
    """
    Représente un problème de programmation linéaire :
    - un objectif (Objective)
    - une liste de contraintes (Constraint).
    """
    def __init__(self, objective, constraints):
        self.objective = objective
        self.constraints = constraints

class Objective:
    """
    Objectif : direction ('max' ou 'min') + une expression.
    """
    def __init__(self, direction, expr):
        self.direction = direction.lower()  # "max" ou "min"
        self.expr = expr

class Constraint:
    """
    Contrainte: left_expr relop right_expr
    relop ∈ { "<=", ">=", "=" }.
    """
    def __init__(self, left_expr, relop, right_expr):
        self.left_expr = left_expr
        self.relop = relop
        self.right_expr = right_expr

# --- Expressions ---
class Expr:
    """Classe mère (abstraite) pour toutes les expressions."""
    pass

class BinOp(Expr):
    """
    Opération binaire : left op right
    op ∈ { '+', '-', '*', '/' }
    """
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(Expr):
    """Un nombre (entier ou flottant)."""
    def __init__(self, value):
        self.value = value

class Var(Expr):
    """Une variable (x1, x2, x3)."""
    def __init__(self, name):
        self.name = name
