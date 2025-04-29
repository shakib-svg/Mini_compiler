from .astt import LPProblem, Objective, Constraint
from .astt import BinOp, Num, Var

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, kind):
        tok = self.current_token()
        if not tok:
            raise Exception(f"Fin de tokens inattendue (attendu={kind}).")
        if tok.kind == kind:
            self.pos += 1
            return tok
        else:
            raise Exception(f"Erreur syntaxique: attendu={kind}, trouvé={tok.kind}({tok.value}).")

    def match(self, kind):
        tok = self.current_token()
        return (tok and tok.kind == kind)

    def parse_lp_problem(self):

        objective = self.parse_objective()
        constraints = []
        while (self.match("ID") or self.match("NUMBER") or self.match("LPAREN")):
            constraints.append(self.parse_constraint())
        return LPProblem(objective, constraints)

    def parse_objective(self):
        if self.match("MAX"):
            direction = self.eat("MAX").value.lower()  
        elif self.match("MIN"):
            direction = self.eat("MIN").value.lower()  
        else:
            raise Exception("Erreur parse_objective: 'max' ou 'min' attendu.")

        self.eat("COLON")      
        expr_node = self.parse_expr()
        self.eat("SEMICOLON")  
        return Objective(direction, expr_node)

    def parse_constraint(self):
        
        left_expr = self.parse_expr()

        tok = self.current_token()
        if not tok:
            raise Exception("Fin inattendue parse_constraint.")
        if tok.kind in ("LE", "GE", "EQ"):
            relop = tok.value  
            self.pos += 1
        else:
            raise Exception(f"Attendu relop <=, >=, =, trouvé={tok.kind}({tok.value}).")

        right_expr = self.parse_expr()
        self.eat("SEMICOLON")
        return Constraint(left_expr, relop, right_expr)

    def parse_expr(self):
        node = self.parse_term()
        while self.match("PLUS") or self.match("MINUS"):
            op = self.current_token().value
            self.eat(self.current_token().kind)
            right = self.parse_term()
            node = BinOp(node, op, right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.match("MULT") or self.match("DIV"):
            op = self.current_token().value
            self.eat(self.current_token().kind)
            right = self.parse_factor()
            node = BinOp(node, op, right)
        return node

    def parse_factor(self):
        tok = self.current_token()
        if not tok:
            raise Exception("Fin inattendue parse_factor.")
        if self.match("NUMBER"):
            self.eat("NUMBER")
            return Num(float(tok.value))
        elif self.match("ID"):
            self.eat("ID")
            return Var(tok.value)
        elif self.match("LPAREN"):
            self.eat("LPAREN")
            node = self.parse_expr()
            self.eat("RPAREN")
            return node
        else:
            raise Exception(f"Token inattendu parse_factor={tok.kind}({tok.value})")
