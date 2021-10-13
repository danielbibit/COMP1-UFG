import logging as log
from compiler.syntax import *

class Analyzer():
    def __init__(self, scanner):
        self.scanner = scanner
        self.error = False
        self.stack = []
        self.stack.append('0')

    def action(self, state, symbol):
        if symbol not in action_table[state]:
            return ('error', symbol)

        elif action_table[state][symbol][0:1] == 'S':
            return ('SHIFT', action_table[state][symbol][1:])

        elif action_table[state][symbol][0:1] == 'R':
            return ('REDUCE', action_table[state][symbol][1:])

        elif action_table[state][symbol] == 'ACCEPT':
            return ('ACCEPT', 'ACCEPT')

        else:
            return ('error', symbol)

    def goto(self, state, non_terminal):
        if non_terminal not in goto_table[state]:
            return False
        else:
            return goto_table[state][non_terminal]

    def run(self):
        scanner_token = self.scanner.tokens()
        recover_token = None

        a = next(scanner_token)

        while True:
            s = self.stack[-1]

            log.debug('Next action state: %s, token: %s', s, a.classe)

            if recover_token:
                next_action = self.action(s, recover_token)
            else:
                next_action = self.action(s, a.classe)

            if(next_action[0] == 'SHIFT'):
                log.debug('shift from %s', self.stack[-1])
                t = next_action[1]

                self.stack.append(t)

                if recover_token:
                    recover_token = None
                else:
                    a = next(scanner_token)

                log.debug('shift to %s', t)
                log.debug('with token: %s', a.classe)
                log.debug('current stack: %s', self.stack)

            elif(next_action[0] == 'REDUCE'):
                log.debug('reduced on %s', self.stack[-1])

                for i in range(grammar_definition[next_action[1]]['len_B']):
                    self.stack.pop()

                log.debug('poped %s items from the stack', grammar_definition[next_action[1]]['len_B'])
                log.debug('current stack: %s', self.stack)

                A = grammar_definition[next_action[1]]['A']
                B = grammar_definition[next_action[1]]['B']

                print(A + ' => ' + B)

                t = self.stack[-1]

                log.debug('t %s', t)

                self.stack.append(self.goto(t, A))

                log.debug('goto %s', self.stack[-1])
                log.debug('with token %s', a.classe)

            elif(next_action[0] == 'ACCEPT'):
                if not self.error:
                    print('OK')
                    return True
                else:
                    print('Syntax analyzer ended with errors. Check output')
                    return False

            else:
                self.error = True

                if a.classe == 'ERRO':
                    print('Lexical error found: ', a.lexema)

                    a = next(scanner_token)

                else:
                    print('\nSyntax error found on: line %d colum %d' % (self.scanner.line, self.scanner.column))

                    expecting_tokens = list(action_table[self.stack[-1]])

                    print('expecting: ', expecting_tokens)
                    print('But instead got: ', next_action[1])

                    #Single token missing, easy fix
                    if len(expecting_tokens) == 1:
                        recover_token = expecting_tokens[0]

                        print('Inserting missing token and recovering\n')
                    #panic
                    else:
                        token_found = False
                        while not token_found:
                            if a.classe in expecting_tokens:
                                token_found = True
                            else:
                                a = next(scanner_token)

                                if a.classe == 'EOF':
                                    print('could not find synch token, EOF')
                                    return False

                        print('Found sync token: %s, resuming...\n' % a.classe)
