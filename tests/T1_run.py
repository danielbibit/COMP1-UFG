# RUN THIS FILE FROM THE ROOT
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import compiler.lexical.scanner as scanner
import compiler.lexical.symbol_table as symbol_table

f = open('tests/resources/descricao_test_file.mgol')
# f = open('tests/resources/invalid_source_test.mgol')
# f = open('tests/resources/valid_source_test.mgol')

s = scanner.Scanner(f)
for token in s.next():
    print(token)
    if token.classe == 'ERRO':
        # exit()
        pass

print('\nSymbol Table:')
for token in symbol_table.symbol_table:
    print(token)
