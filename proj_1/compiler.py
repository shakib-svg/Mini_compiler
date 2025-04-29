from .lexer import Lexer
from .parser import Parser
from .visitors import PrettyPrinterVisitor
from .solver import SimpleLPSolver

class LPCompiler:
    def __init__(self):
        self.solver = SimpleLPSolver()

    def compile(self, input_text):

       
        lexer = Lexer(input_text)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        lp_ast = parser.parse_lp_problem()
        printer = PrettyPrinterVisitor()
        print("=== LP Problem (pretty printed) ===")
        print(printer.visit(lp_ast))
        print("====================================")
        solution = self.solver.solve(lp_ast)
        return solution
