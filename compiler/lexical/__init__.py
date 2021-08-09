import string

from compiler.lexical.automata_definition import transitions
from compiler.lexical.automata_definition import final_states

letters = string.ascii_lowercase + string.ascii_uppercase
L = [i for i in letters]
D = [str(i) for i in range(10)]
valid = ['+', '-', '/', '*', '(', ')', '<', '>', '=', '{', '}', ';', ',','.', '\n', '\t', ' ', '_', '\'', '\"']
alphabet = L + D + valid

def automaton(current_state, character):
    if current_state in transitions:
        # single character is availabe. It has priority (q11 and q15)
        if character in transitions[current_state]:
            return transitions[current_state][character]
        # the transition takes any valid input (), q0 can't have ANYTHING transition!!!
        elif 'ANYTHING' in transitions[current_state]:
            if character in alphabet:
                return transitions[current_state]['ANYTHING']
        else:
            if character in L:
                # Rule exception for num type
                if current_state in ['q1', 'q3']:
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

            return transitions[current_state][symbol]

    return False #current_state don't have a transition

def scanner(string):
    current_state = 'q0'

    for c in string:
        current_state = automaton(current_state, c)

        if current_state == False:
            print('error ' + c)
            return

    if current_state in final_states:
        print('ok ' + current_state + ' ' + final_states[current_state] + ' ' + string)
        # yield
    else:
        print(current_state + 'not ok')
