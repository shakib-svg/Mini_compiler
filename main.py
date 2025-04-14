# main.py

import sys
from .compiler import LPCompiler




def main():
    if len(sys.argv) < 2:
        print("Usage: python3 -m proj_1.main <fichier.lp>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        text = f.read()

    compiler = LPCompiler()
    solution = compiler.compile(text)
    if solution:
        print("\n=== SOLUTION ===")
        for k,v in solution.items():
            print(f"{k} = {v}")
        print("================")

if __name__ == "__main__":
    main()
