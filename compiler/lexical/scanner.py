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
            print('Files should end with a \\n, exiting...')
            exit()

        self.source = source
        self.source_size = len(source)
        self.count = -1
        self.line = 1
        self.column = 0
        self.current_state = 'q0'
        self.previous_state = 'q0'
        self.buffer = ''

    def automaton(self, character):
        if self.current_state in transitions:
            if character in transitions[self.current_state]:
                return transitions[self.current_state][character]
            else:
                return False

        #current_state don't have a transition
        return False

    def classify_token(self, token):
        if token.classe == 'id':
            if not is_identifier(token.lexema):
                symbol_table.append(token)
            else:
                token = get_token_id(token.lexema)

        elif token.classe == 'lit':
            token.tipo = 'literal'

        elif token.classe == 'num':
            if '.' in token.lexema:
                token.tipo = 'real'
            else:
                token.tipo = 'inteiro'

        return token

    def tokens(self):
        while self.count < self.source_size-1:
            self.count += 1
            self.column += 1
            base_message = 'Error on line ' + str(self.line) + ' column ' + str(self.column) + ', '

            if self.current_state == 'q0':
                self.buffer = ''

            c = self.source[self.count]

            if c == '\n':
                #Literals can't be multi line, by the regex defintion
                if self.current_state == 'q11':
                    yield Token('ERRO', base_message + 'incomplete literal', 'NULO')

                    self.current_state = 'q0'

                self.line += 1
                self.column = 0

            self.buffer += c

            self.previous_state = self.current_state
            self.current_state = self.automaton(c)

            #Error treatment when no trasition is found
            if self.current_state == False:
                #Something went wrong, and we are left with a incomplete literal or comment in the buffer
                if self.previous_state== 'q11':
                    yield Token('ERRO', base_message + 'incomplete literal', 'NULO')

                if self.previous_state == 'q15':
                    yield Token('ERRO', base_message + 'incomplete comment', 'NULO')

                #Verify if we got here by a invalid character
                if c not in alphabet:
                    message = 'the character \''+ c + '\' is not valid in this language.'
                    yield Token('ERRO', base_message + message, 'NULO')

                #keep reading as if nothign ever happened
                self.current_state = 'q0'

            if self.current_state in final_states:
                #We are on a final state, and the next char is invalid, we found a token!!!
                if self.automaton(self.source[self.count + 1]) == False:
                    token = Token(final_states[self.current_state], self.buffer, 'NULO')

                    if (token.classe == 'COMENT'):
                        pass
                    else:
                        yield self.classify_token(token)

                    self.current_state = 'q0'
                    self.buffer = ''

        if self.current_state == 'q15':
            yield Token('ERRO','End of file, and you forgot to close your comment with }', 'NULO')

        yield Token('EOF', 'EOF', 'NULO')
