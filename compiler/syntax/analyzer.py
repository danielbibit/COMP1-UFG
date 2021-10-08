from compiler.syntax import *

stack = []
stack.append('0')
class Analyzer():
    def __init__(self, scanner):
        self.scanner = scanner

    def action(self, state, symbol):
        if symbol not in action_table[state]:
            return ('error', 'error')
        elif action_table[state][symbol][0:1] == 'S':
            return ('SHIFT', action_table[state][symbol][1:])
        elif action_table[state][symbol][0:1] == 'R':
            return ('REDUCE', action_table[state][symbol][1:])
        elif action_table[state][symbol] == 'ACCEPT':
            return ('ACCEPT', 'ACCEPT')
        else:
            return ('error', 'error')

    def goto(self, state, non_terminal):
        if non_terminal not in goto_table[state]:
            return False
        else:
            return goto_table[state][non_terminal]

    def run(self):
        scanner_iterator = self.scanner.next()
        a = next(scanner_iterator).classe
        t = 0

        print('first Token: ', a)
        while True:
            s = stack[-1]

            next_action = self.action(s, a)

            if(next_action[0] == 'SHIFT'):
                print('shift from ', stack[-1])
                t = next_action[1]

                stack.append(t)

                a = next(scanner_iterator).classe
                print('shift to ', t)
                print('new token: ', a)
            elif(next_action[0] == 'REDUCE'):
                print('reduced on ', stack[-1])

                for i in range(grammar_definition[next_action[1]]['len_B']):
                    stack.pop()


                t = stack[-1]

                A = grammar_definition[next_action[1]]['A']
                B = grammar_definition[next_action[1]]['B']
                print(A + ' => ' + B)

                print('t ', t)
                stack.append(self.goto(t, A))
                print('goto ', stack[-1])
                print('with token ', a)
            elif(next_action[0] == 'ACCEPT'):
                print('entrei 3')
                print(next_action[1])

            else:
                print('entrei 4')
                return

            input()

