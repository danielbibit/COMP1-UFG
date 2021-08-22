from io import IOBase
from compiler.lexical.automaton_definition import transitions
from compiler.lexical.automaton_definition import final_states
from compiler.lexical.automaton_definition import L, D, alphabet
from compiler.lexical.token import Token
from compiler.lexical.symbol_table import *


class Scanner():
    def __init__(self, source):
        #Convert file to string
        if isinstance(source, IOBase):
            temp = ''
            with source:
                temp = source.read()

            source = temp

        #POSIX files should end with a \n
        if source[-1] != '\n':
            print('File should end with a \\n, exiting...')
            exit()

        self.source = source
        self.source_size = len(source)
        self.count = -1
        self.line = 1
        self.column = 0
        self.current_state = 'q0'
        self.buffer = ''

    def automaton(self, character):
        if self.current_state in transitions:
            if character in transitions[self.current_state]:
                return transitions[self.current_state][character]
            else:
                return False

        #current_state don't have a transition
        return False

    def error_message(self, error_character):
        if self.current_state == 'q0':
            return 'Error on line ' + str(self.line) + ' column ' + str(self.column) + ', the character \'' \
            + error_character + '\' is not valid in this language.'
        else:
            return 'Undefined lexical error'

    def classify_token(self, token):
        if token.classe == 'ID':
            if not is_identifier(token.lexema):
                symbol_table.append(token)

        elif token.classe == 'LIT':
            token.tipo = 'literal'

        elif token.classe == 'NUM':
            if '.' in token.lexema:
                token.tipo = 'real'
            else:
                token.tipo = 'inteiro'

        return token

    def next(self):
        #Iterate the file char by char. The last MUST be a \n
        while self.count < self.source_size-1:
            self.count += 1
            self.column += 1

            # if self.current_state == 'q0':
            #     self.buffer = ''

            c = self.source[self.count]

            if c == '\n':
                self.line += 1
                self.column = 0

            self.buffer += c
            self.current_state = self.automaton(c)

            if self.current_state == False:
                # self.current_state = 'q0'
                yield Token('ERRO', self.error_message(c), 'NULO')

            if self.current_state in final_states:
                #We are on a final state, and the next char is invalid, we found a token!
                if self.automaton(self.source[self.count + 1]) == False:
                    token = Token(final_states[self.current_state], self.buffer, 'NULO')

                    yield self.classify_token(token)

                    self.current_state = 'q0'
                    self.buffer = ''

        yield Token('EOF', 'EOF', 'NULO')
