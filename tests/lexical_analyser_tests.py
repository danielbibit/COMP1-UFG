# RUN THIS FILE FROM THE ROOT
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import compiler.lexical.scanner as scanner
import compiler.lexical.symbol_table as symbol_table
test_strings = [
    '2334\n', '2.4a\n', '2.8e10\n', '3.5e-8\n','2E-10\n',
    '\'>\'\n', '\"Daniel2.\"\n',
    'Animal\n', 'Dan_1\n',
    '{daniel+1}\n',
    '<=\n','<>\n','>\n','>=\n',
    '<-\n',
    '+\n',
    '+-\n',
]

# f = open('tests/tokens_test.mgol')
f = open('tests/valid_source_test.mgol')
# f = open('tests/invalid_source_test.mgol')

with f:
    f1 = f.read()


s = scanner.Scanner(f1)
for token in s.next():
    print(token)

print(symbol_table.symbol_table)

# for s in test_strings:
#     print('Current test string: ', s)
#     scanner = lexical.Scanner(s)
#     # print(next(scanner.next()))
#     for token in scanner.next():
#         print(token)

