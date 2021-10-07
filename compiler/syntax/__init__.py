import csv

action = {}
with open('compiler/syntax/action.csv') as csv_file:
    data = csv.DictReader(csv_file, delimiter=',')

    for line in data:
        state = line['state']
        del line['state']
        action[state] = {}
        for non_terminal, transition in line.items():
            if transition != '':
                action[state][non_terminal] = transition


goto = {}
with open('compiler/syntax/goto.csv') as csv_file:
    data = csv.DictReader(csv_file, delimiter=',')

    for line in data:
        state = line['state']
        del line['state']
        goto[state] = {}
        for non_terminal, transition in line.items():
            if transition != '':
                goto[state][non_terminal] = transition

# grammar = {}
# with open('docs/')
