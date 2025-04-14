# visitors.py

from .astt import LPProblem, Objective, Constraint
from .astt import BinOp, Num, Var

class NodeVisitor:
    """
    Visiteur de base.
    On appelle visit(node) => dispatch sur visit_<ClassName>.
    """
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{type(node).__name__} method in {type(self).__name__}.")

class PrettyPrinterVisitor(NodeVisitor):
    """
    Pour réafficher un problème LP.
    """
    def visit_LPProblem(self, node: LPProblem):
        s = []
        s.append(self.visit(node.objective))
        s.append("Subject to:\n")
        for c in node.constraints:
            s.append("  " + self.visit(c))
        return "".join(s)

    def visit_Objective(self, node: Objective):
        direction = node.direction.upper()  # "MAX" ou "MIN"
        expr_str = self.visit(node.expr)
        return f"{direction}: {expr_str};\n"

    def visit_Constraint(self, node: Constraint):
        left_str = self.visit(node.left_expr)
        right_str = self.visit(node.right_expr)
        return f"{left_str} {node.relop} {right_str};\n"

    def visit_BinOp(self, node: BinOp):
        left_s = self.visit(node.left)
        right_s = self.visit(node.right)
        return f"({left_s} {node.op} {right_s})"

    def visit_Num(self, node: Num):
        return str(node.value)

    def visit_Var(self, node: Var):
        return node.name
