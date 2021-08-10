import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

import compiler.lexical.scanner as scanner
import compiler.lexical.symbol_table as symbol_table
import compiler.lexical.token as token

class TestLexical(unittest.TestCase):
    def setUp(self):
        self.strings_num = [
            '2334\n', '2.4a\n', '2.8e10\n', '3.5e-8\n','2E-10\n',
        ]

        self.strings_lit = [
            '\'x\'\n', '\"Daniel2.\"\n',
        ]

        self.strings_id = [
            'Animal\n', 'Dan_1\n',
        ]

        self.strings_coments = [
            '{daniel+1}\n', '{sdfwfasa\sd.sdfwa}\n',
        ]

        self.strings_relacionais = [
            '<\n', '>\n', '<=\n', '<>\n','>=\n',
        ]

    def test_single_tokens(self):
        everything = self.strings_num + self.strings_lit + self.strings_id + self.strings_coments + self.strings_relacionais

        for string in everything:
            s = scanner.Scanner(string)
            for token in s.next():
                self.assertNotEqual(token.classe, 'ERRO')

    def test_eof(self):
        for string in self.strings_num:
            last_token = token.Token('','','')

            s = scanner.Scanner(string)
            for t in s.next():
                last_token = t

            self.assertEqual(last_token.classe, 'EOF')

    def test_valid_code(self):
        f = open('tests/valid_source_test.mgol')
        with f:
            f1 = f.read()
        s = scanner.Scanner(f1)
        for token in s.next():
            self.assertNotEqual(token.classe, 'ERRO')


if __name__ == '__main__':
    unittest.main()
