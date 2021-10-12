import logging as log
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
        scanner_iterator = self.scanner.tokens()
        a = next(scanner_iterator).classe
        t = 0

        log.debug('first Token: %s', a)
        while True:
            s = stack[-1]

            next_action = self.action(s, a)

            if(next_action[0] == 'SHIFT'):
                log.debug('shift from %s', stack[-1])
                t = next_action[1]

                stack.append(t)

                a = next(scanner_iterator).classe
                log.debug('shift to %s', t)
                log.debug('new token: %s', a)
            elif(next_action[0] == 'REDUCE'):
                log.debug('reduced on %s', stack[-1])

                count = 0
                for i in range(grammar_definition[next_action[1]]['len_B']):
                    stack.pop()
                    count += 1
                log.debug('poped %s items from the stack', count, )
                log.debug('current stack: %s', stack)
                t = stack[-1]

                A = grammar_definition[next_action[1]]['A']
                B = grammar_definition[next_action[1]]['B']

                tab = ''
                # for i in range(len(stack)):
                #     tab += '  '
                print(tab + A + ' => ' + B)

                log.debug('t %s', t)

                stack.append(self.goto(t, A))

                log.debug('goto %s', stack[-1])
                log.debug('with token %s', a)
            elif(next_action[0] == 'ACCEPT'):
                print(next_action[1])
                return
            else:
                print('entrei 4')
                return

            # input()
            # print()

