import string

from compiler.lexical.automata_definition import transitions
from compiler.lexical.automata_definition import final_states
from compiler.lexical.token import Token

letters = string.ascii_lowercase + string.ascii_uppercase
L = [i for i in letters]
D = [str(i) for i in range(10)]
valid = ['+', '-', '/', '*', '(', ')', '<', '>', '=', '{', '}', ';', ',','.', '\n', '\t', ' ', '_', '\'', '\"', '\\']
alphabet = L + D + valid

class Scanner():
    def __init__(self, source):
        self.source = source
        self.source_size = len(source)
        self.count = -1
        self.current_state = 'q0'
        self.buffer = ''

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
            #FIXME generalize this structure
            else:
                if character in L:
                    # Rule exception for num type
                    if self.current_state in ['q1', 'q3']:
                        if character in ['e', 'E']:
                            symbol = character
                        else:
                            return False #Processing a num, recived invalid character
                    else:
                        symbol = 'CHARACTER'
                elif character in D:
                    symbol = 'DIGIT'
                else:
                    return False #The symbol is not valid, expecting char or num

                #Verify if exist a transition for this symbol
                if symbol in transitions[self.current_state]:
                    return transitions[self.current_state][symbol]
                else:
                    return False

        return False #current_state don't have a transition

    def next(self):
        # print('got into next, with source size ', self.source_size)
        runs = 0
        while self.count < self.source_size:
            self.count += 1

            if self.current_state == 'q0':
                self.buffer = ''

            c = self.source[self.count]
            # print('current c', c)
            self.buffer += c
            self.current_state = self.automaton(c)
            # print('got to state', self.current_state)

            if self.current_state == False:
                yield Token('ERRO', 'errotext', 'NULO')
                # yield 'error ' + c
                self.current_state = 'q0'

            if self.current_state in final_states:
                # print('in a final state')
                # print('next char is ', self.source[self.count + 1])
                if self.automaton(self.source[self.count + 1]) == False:
                    yield Token(final_states[self.current_state], self.buffer, 'NULO')
                    # yield 'ok ' + self.current_state + ' ' + final_states[self.current_state] + ' ' + self.buffer
                    self.current_state = 'q0'
