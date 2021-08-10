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
        '\t':'q0',
        ' ':'q0',
        '\n': 'q0',
        'DIGIT': 'q1',
        '\'': 'q7',
        '\"': 'q10',
        'CHARACTER': 'q13',
        '{': 'q14',
        '<': 'q18',
        '=': 'q19',
        '>': 'q21',
        '+': 'q22',
        '-': 'q22',
        '/': 'q22',
        '*': 'q22',
        '(': 'q23',
        ')': 'q24',
        ';': 'q25',
        ',': 'q26',
    },
    'q1':{
        'DIGIT':'q1',
        'E':'q4',
        'e':'q4',
        '.':'q2',
    },
    'q2':{
        'DIGIT':'q3',
    },
    'q3':{
        'DIGIT':'q3',
        'E':'q4',
        'e':'q4',
    },
    'q4':{
        '+': 'q5',
        '-': 'q5',
        'DIGIT': 'q6',
    },
    'q5':{
        'DIGIT': 'q6',
    },
    'q6':{
        'DIGIT': 'q6',
    },
    'q7':{
        'ANYTHING': 'q8',
    },
    'q8':{
        '\'': 'q9',
    },
    'q10':{
        'ANYTHING': 'q11',
    },
    'q11':{
        'ANYTHING': 'q11',
        '\"': 'q12',
    },
    'q13':{
        'CHARACTER': 'q13',
        'DIGIT': 'q13',
        '_': 'q13',
    },
    'q14':{
        'ANYTHING': 'q15',
    },
    'q15':{
        'ANYTHING': 'q15',
        '}': 'q16',
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