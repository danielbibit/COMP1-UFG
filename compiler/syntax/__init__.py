import csv

action_table = {}
with open('compiler/syntax/action.csv') as csv_file:
    data = csv.DictReader(csv_file, delimiter=',')

    for line in data:
        state = line['state']
        del line['state']
        action_table[state] = {}
        for non_terminal, transition in line.items():
            if transition != '':
                action_table[state][non_terminal] = transition


goto_table = {}
with open('compiler/syntax/goto.csv') as csv_file:
    data = csv.DictReader(csv_file, delimiter=',')

    for line in data:
        state = line['state']
        del line['state']
        goto_table[state] = {}
        for non_terminal, transition in line.items():
            if transition != '':
                goto_table[state][non_terminal] = transition


grammar_definition = {}
with open('docs/grammar.txt') as f:

    for line_number, line in enumerate(f):
        rule = {}
        rule_split = line.replace('\n', '').split('=>')
        rule['A'] = rule_split[0].replace(' ', '')
        rule['B'] = rule_split[1][1:]
        rule['len_B'] = len(rule['B'].split(' '))

        grammar_definition[str(line_number+1)] = rule
