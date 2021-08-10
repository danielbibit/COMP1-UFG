import string
letters = string.ascii_lowercase + string.ascii_uppercase

L = [i for i in letters]
D = [str(i) for i in range(10)]

valid = [
    '+', '-', '/', '*',
    '(', ')',
    '<', '>', '=',
    '{', '}',
    ';', ',','.', '_',
    '\'', '\"',
    '\\',
    '\n', '\t', ' '
]

alphabet = L + D + valid

transitions = {
    'q0':{
        '\'': 'q7',
        '\"': 'q10',
        '{': 'q14',
        '<': 'q18',
        '=': 'q19',
        '>': 'q21',
        '(': 'q23',
        ')': 'q24',
        ';': 'q25',
        ',': 'q26',
    },
    'q1':{
        'E':'q4',
        'e':'q4',
        '.':'q2',
    },
    'q3':{
        'E':'q4',
        'e':'q4',
    },
    'q4':{
        '+': 'q5',
        '-': 'q5',
    },
    'q8':{
        '\'': 'q9',
    },
    'q13':{
        '_': 'q13',
    },
    'q18':{
        '>': 'q19',
        '=': 'q19',
        '-': 'q20',
    },
    'q21':{
        '=':'q19',
    }
}

def populate_transitions(symbol_list, origin_state_list, next_state):
    for c in symbol_list:
        for state in origin_state_list:
            if state not in transitions:
                transitions[state] = {}

            transitions[state][c] = next_state

populate_transitions([' ', '\n', '\t'], ['q0'], 'q0')

populate_transitions(['+', '-', '/', '*' ], ['q0'], 'q22')


populate_transitions(D, ['q0', 'q1'], 'q1')
populate_transitions(D, ['q2', 'q3'], 'q3')
populate_transitions(D, ['q4', 'q5', 'q6'], 'q6')
populate_transitions(D, ['q13'], 'q13')

populate_transitions(L, ['q0', 'q13'], 'q13')

populate_transitions(alphabet, ['q7'], 'q8')
populate_transitions(alphabet, ['q10', 'q11'], 'q11')
populate_transitions(alphabet, ['q14', 'q15'], 'q15')

#Close " and }
transitions['q11']['\"'] = 'q12'
transitions['q15']['}'] = 'q16'

final_states = {
    'q1': 'NUM',
    'q3': 'NUM',
    'q6': 'NUM',
    'q9': 'LIT',
    'q12': 'LIT',
    'q13': 'ID',
    'q16': 'COMENT',
    'q18': 'OPR',
    'q19': 'OPR',
    'q20': 'RCB',
    'q21': 'OPR',
    'q22': 'OPM',
    'q23': 'AB_P',
    'q24': 'FC_P',
    'q25': 'PT_V',
    'q26': 'VIR'
}
