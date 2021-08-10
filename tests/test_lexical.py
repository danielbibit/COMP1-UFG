import os, sys

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

        self.full_strings = [
            'se(B>2);B<-B+1;\n',
        ]


    def test_single_tokens(self):
        everything = self.strings_num + self.strings_lit + self.strings_id + self.strings_coments + self.strings_relacionais

        for string in everything:
            s = scanner.Scanner(string)
            for token in s.next():
                self.assertNotEqual(token.classe, 'ERRO')


    def test_eof(self):
        for string in self.strings_num:
            s = scanner.Scanner(string)

            tokens = [t for t in s.next()]

            self.assertEqual(tokens[-1].classe, 'EOF')

        #Test whole source code
        f = open('tests/valid_source_test.mgol')
        with f:
            f1 = f.read()

        s = scanner.Scanner(f1)

        tokens = [t for t in s.next()]

        self.assertEqual(tokens[-1].classe, 'EOF')


    def test_valid_source_code(self):
        f = open('tests/valid_source_test.mgol')
        with f:
            f1 = f.read()
        s = scanner.Scanner(f1)
        for token in s.next():
            self.assertNotEqual(token.classe, 'ERRO')


    @unittest.expectedFailure
    def test_invalid_source_code(self):
        f = open('tests/invalid_source_test.mgol')
        with f:
            f1 = f.read()
        s = scanner.Scanner(f1)
        for token in s.next():
            self.assertNotEqual(token.classe, 'ERRO')


if __name__ == '__main__':
    unittest.main()
