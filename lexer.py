# lexer.py
import re

class Token:
    """Représente un jeton lexical (kind, value)."""
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __repr__(self):
        return f"Token({self.kind}, {self.value})"

class Lexer:
    """
    Lexer à base de regex.
    Gère max, min, <=, >=, =, +, -, *, /, chiffres, identifiants (x1, x2, x3, etc.), ...
    """
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.rules = [
            (r'[ \t\n]+',           None),     # espaces
            (r'#.*',                None),     # commentaire style "#..."
            (r'max\b',             'MAX'),
            (r'min\b',             'MIN'),
            (r':',                 'COLON'),
            (r';',                 'SEMICOLON'),
            (r'<\=',               'LE'),  # <=
            (r'>\=',               'GE'),  # >=
            (r'\=',                'EQ'),  # =
            (r'\+',                'PLUS'),
            (r'-',                 'MINUS'),
            (r'\*',                'MULT'),
            (r'\/',                'DIV'),
            (r'\(',                'LPAREN'),
            (r'\)',                'RPAREN'),
            (r'[0-9]+(\.[0-9]+)?', 'NUMBER'),   # int ou float
            (r'[a-zA-Z_]\w*',      'ID'),       # ex: x1, x2, x3, ...
        ]

    def tokenize(self):
        tokens = []
        while self.pos < len(self.text):
            match_found = False
            for pattern, kind in self.rules:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos)
                if match:
                    if kind is not None:
                        tokens.append(Token(kind, match.group(0)))
                    self.pos = match.end()
                    match_found = True
                    break
            if not match_found:
                snippet = self.text[self.pos:self.pos+10]
                raise Exception(f"Erreur lexicale à pos={self.pos} près de '{snippet}'")
        return tokens
