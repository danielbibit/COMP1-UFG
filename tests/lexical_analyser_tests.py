import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import compiler.lexical as lexical

test_strings = [
    '23', '2.4a', '2.8e10', '3.5e-8','2E-10',
    '\'>\'', '\"Daniel2.\"',
    'Animal', 'Dan_1',
    '{daniel+1}',
    '<=','<>','>','>=',
    '<-',
    '+',
    '+-',
]

for s in test_strings:
    lexical.scanner(s)
