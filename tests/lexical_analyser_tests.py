# RUN THIS FILE FROM THE ROOT
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import compiler.lexical.scanner as scanner
import compiler.lexical.symbol_table as symbol_table

# f = open('tests/tokens_test.mgol')
f = open('tests/valid_source_test.mgol')
# f = open('tests/invalid_source_test.mgol')

with f:
    f1 = f.read()

s = scanner.Scanner(f1)
for token in s.next():
    print(token)

print('\nSymbol Table:')
for token in symbol_table.symbol_table:
    print(token)
