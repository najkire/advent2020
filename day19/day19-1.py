import re

with open('input.txt', 'r') as input_file:
    rules, input = [], []
    line = input_file.readline().strip()
    while line:
        rules += [line]
        line = input_file.readline().strip()

    line = input_file.readline().strip()
    while line:
        input += [line]
        line = input_file.readline().strip()

rule_dict = {rule.split(':')[0]: rule.split(':')[1].strip() for rule in rules}

main_rule = rule_dict['0']
while re.search(r'\d', main_rule):
    main_rule = ' '.join([f'( {rule_dict[c]} )' if re.match(r'\d+', c) else c for c in main_rule.split()])

re_rule = '^' + main_rule.replace('( "', '').replace('" )', '').replace(' ', '') + '$'
print(sum([re.match(re_rule, i) is not None for i in input]))
