# RUN THIS FILE FROM THE ROOT
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import compiler.lexical as lexical

test_strings = [
    '2334\n', '2.4a\n', '2.8e10\n', '3.5e-8\n','2E-10\n',
    '\'>\'', '\"Daniel2.\"',
    'Animal', 'Dan_1',
    '{daniel+1}',
    '<=','<>','>','>=',
    '<-',
    '+',
    '+-',
]

# f = open('tests/tokens_test.mgol')
f = open('tests/valid_source_test.mgol')
# f = open('tests/invalid_source_test.mgol')

with f:
    f1 = f.read()


scanner = lexical.Scanner(f1)
for token in scanner.next():
    print(token)

# for s in test_strings:
#     scanner = lexical.Scanner(s)
#     scanner.next()
