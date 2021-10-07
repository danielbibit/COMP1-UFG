import compiler.lexical.scanner as scanner
import compiler.syntax as syntax

stack = []
stack.append(0)


f = open('tests/resources/descricao_test_file.mgol')
scan = scanner.Scanner(f)

for token in scan.next():
    s = stack[-1]
    if(syntax.action[stack][token.classe][0] == 'S'):
        pass
    elif(syntax.action[stack][token.classe][0] == 'R'):
        pass
    elif(syntax.action[stack][token.classe] == 'ACCEPT'):
        pass
    else:
        pass
