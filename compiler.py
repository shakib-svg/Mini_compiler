# compiler.py

from .lexer import Lexer
from .parser import Parser
from .visitors import PrettyPrinterVisitor
from .solver import SimpleLPSolver

class LPCompiler:
    """
    Orchestration du mini-compilateur LP (3 variables).
    """
    def __init__(self):
        self.solver = SimpleLPSolver()

    def compile(self, input_text):
        """
        1) Lexing
        2) Parsing => AST
        3) Pretty print
        4) Solve => renvoie un dictionnaire de solution
        """
        # 1) Lexer
        lexer = Lexer(input_text)
        tokens = lexer.tokenize()

        # 2) Parser
        parser = Parser(tokens)
        lp_ast = parser.parse_lp_problem()

        # 3) PrettyPrinter
        printer = PrettyPrinterVisitor()
        print("=== LP Problem (pretty printed) ===")
        print(printer.visit(lp_ast))
        print("====================================")

        # 4) Solve
        solution = self.solver.solve(lp_ast)
        return solution
