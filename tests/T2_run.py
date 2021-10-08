import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import compiler.syntax as syntax

# print(syntax.goto['state'])
# print(syntax.action['0']['P'])
# print(syntax.action)

print(syntax.grammar)
