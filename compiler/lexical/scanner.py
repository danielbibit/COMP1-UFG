from compiler.lexical.automaton_definition import transitions
from compiler.lexical.automaton_definition import final_states
from compiler.lexical.automaton_definition import L, D, alphabet
from compiler.lexical.token import Token
from compiler.lexical.symbol_table import *


class Scanner():
    def __init__(self, source):
        self.source = source
        self.source_size = len(source)
        self.count = -1
        self.line = 1
        self.column = 0
        self.current_state = 'q0'
        self.buffer = ''

        if source[-1] != '\n':
            print('File should end with a \\n, exiting...')
            exit()

    def automaton(self, character):
        if self.current_state in transitions:
            # single character is availabe. It has priority (q11 and q15)
            if character in transitions[self.current_state]:
                return transitions[self.current_state][character]
            # the transition takes any valid input (), q0 can't have ANYTHING transition!!!
            elif 'ANYTHING' in transitions[self.current_state]:
                if character in alphabet:
                    return transitions[self.current_state]['ANYTHING']
            #Verify if is a CHARACTER or DIGIT then verify if has transitions
            else:
                if character in L:
                    # Rule exception for num type
                    if self.current_state in ['q1', 'q3']:
                        if character in ['e', 'E']:
                            symbol = character
                        else:
                            #Processing a num, recived invalid character
                            return False
                    else:
                        symbol = 'CHARACTER'
                elif character in D:
                    symbol = 'DIGIT'
                else:
                    #The symbol is not valid, expecting char or num
                    return False

                #Verify if exist a transition for this symbol
                if symbol in transitions[self.current_state]:
                    return transitions[self.current_state][symbol]
                else:
                    return False

        return False #current_state don't have a transition

    def next(self):
        while self.count < self.source_size-1:
            self.count += 1
            self.column += 1

            if self.current_state == 'q0':
                self.buffer = ''

            c = self.source[self.count]
            if c == '\n':
                self.line += 1
                self.column = 0

            self.buffer += c
            self.current_state = self.automaton(c)

            if self.current_state == False:
                yield Token('ERRO', 'ln '+str(self.line)+' col: ' + str(self.column), 'NULO')
                self.current_state = 'q0'

            if self.current_state in final_states:
                if self.automaton(self.source[self.count + 1]) == False:
                    token = Token(final_states[self.current_state], self.buffer, 'NULO')

                    if token.classe == 'ID':
                        in_table = is_identifier(token.lexema)
                        if in_table:
                            yield in_table
                        else:
                            symbol_table.append(token)
                            yield token
                    elif token.classe == 'LIT':
                        token.tipo == 'literal'
                        yield token
                    elif token.classe == 'NUM':
                        if '.' in token.lexema:
                            token.tipo = 'real'
                        else:
                            token.tipo = 'inteiro'
                        yield token
                    else:
                        yield token

                    self.current_state = 'q0'

        yield Token('EOF', 'EOF', 'NULO')
