# solver.py

import numpy as np
from .astt import BinOp, Num, Var

class SimpleLPSolver:
    """
    Solveur minimaliste pour 3 variables : x1, x2, x3.
    Gère : (a1*x1 + a2*x2 + a3*x3 + c).
    Toute multiplication var*var => Exception.
    On renvoie une solution factice.
    """

    def solve(self, lp_ast):
        # Récupère la direction
        direction = lp_ast.objective.direction  # "max" ou "min"

        # On extrait l'objectif: (a1, a2, a3), c_obj
        a_obj, c_obj = self.extract_expr(lp_ast.objective.expr)

        # Construit A, b, sense pour les contraintes
        A = []
        b = []
        sense = []  # "L", "G", "E"

        for cstr in lp_ast.constraints:
            a_left, c_left = self.extract_expr(cstr.left_expr)
            a_right, c_right = self.extract_expr(cstr.right_expr)

            # On ramène tout à gauche => a_left - a_right
            # ex: a_left x <= a_right x => (a_left-a_right) x <= 0
            a_c = (a_left[0] - a_right[0],
                   a_left[1] - a_right[1],
                   a_left[2] - a_right[2])
            c_c = c_left - c_right

            if cstr.relop == "<=":
                sense.append("L")  # <=
                A.append(a_c)
                b.append(-c_c)
            elif cstr.relop == ">=":
                sense.append("G")  # >=
                A.append(a_c)
                b.append(-c_c)
            elif cstr.relop == "=":
                sense.append("E")  # =
                A.append(a_c)
                b.append(-c_c)
            else:
                raise Exception(f"Relop inconnu: {cstr.relop}")

        print(f"[Solveur] (Fictif) 3 var => direction={direction}, obj=(a1={a_obj[0]}, a2={a_obj[1]}, a3={a_obj[2]}, c={c_obj})")
        # On n'implémente pas d'algo : on rend une solution bidon.
        return {
            "x1": 1.0,
            "x2": 2.0,
            "x3": 3.0,
            "objective_value": 999.0
        }

    def extract_expr(self, expr):
        """
        Extrait ( (a1,a2,a3), c ) pour une expression linéaire en x1,x2,x3.
        """
        if isinstance(expr, Num):
            return (0.0, 0.0, 0.0), expr.value

        if isinstance(expr, Var):
            name = expr.name.lower()
            if name == "x1":
                return (1.0, 0.0, 0.0), 0.0
            elif name == "x2":
                return (0.0, 1.0, 0.0), 0.0
            elif name == "x3":
                return (0.0, 0.0, 1.0), 0.0
            else:
                raise Exception(f"Variable inconnue '{expr.name}', on attend x1, x2, x3.")

        if isinstance(expr, BinOp):
            left_a, left_c = self.extract_expr(expr.left)
            right_a, right_c = self.extract_expr(expr.right)

            op = expr.op
            if op == '+':
                return ((left_a[0] + right_a[0],
                         left_a[1] + right_a[1],
                         left_a[2] + right_a[2]),
                        left_c + right_c)

            elif op == '-':
                return ((left_a[0] - right_a[0],
                         left_a[1] - right_a[1],
                         left_a[2] - right_a[2]),
                        left_c - right_c)

            elif op == '*':
                # autoriser var * cste
                if self.is_constant(left_a):
                    return self.mul_const(left_c, right_a, right_c)
                elif self.is_constant(right_a):
                    return self.mul_const(right_c, left_a, left_c)
                else:
                    raise Exception("Multiplication var*var => non linéaire.")

            elif op == '/':
                # autorisé seulement si le dénominateur est constant
                if not self.is_constant(right_a):
                    raise Exception("Division par expr variable => non linéaire.")
                if abs(right_c) < 1e-12:
                    raise Exception("Division par zéro.")
                new_a = (left_a[0]/right_c, left_a[1]/right_c, left_a[2]/right_c)
                new_c = left_c / right_c
                return new_a, new_c

            else:
                raise Exception(f"Opérateur inconnu: {op}")

        raise Exception("Expression non gérée ou non linéaire.")

    def is_constant(self, a):
        """Check si (a1, a2, a3) == (0,0,0)."""
        return (abs(a[0]) < 1e-12) and (abs(a[1]) < 1e-12) and (abs(a[2]) < 1e-12)

    def mul_const(self, cst, a, c):
        """
        cst*(a.x + c) => (cst*a, cst*c).
        a = (a1,a2,a3), c = cste
        """
        return ((a[0]*cst, a[1]*cst, a[2]*cst),
                c*cst)
