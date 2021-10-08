import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import compiler.lexical.scanner as scanner
import compiler.syntax as syntax
import compiler.syntax.analyzer as analyzer

f = open('tests/resources/t2_source.mgol')
s = scanner.Scanner(f)

a = analyzer.Analyzer(s)

a.run()
