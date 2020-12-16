import re

with open('input.txt', 'r') as input_file:
    input = [line.strip() for line in input_file.readlines()]

rules = {}
rule_re = re.compile(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)')

for n, line in enumerate(input):
    if rule_re.match(line):
        field_range = rule_re.match(line).groups()
        rules[field_range[0]] = field_range[1:]      
    if 'your ticket' in line:
        my_ticket = input[n + 1]
    if 'nearby tickets' in line:
        nearby_tickets = input[n + 1:] 

valid_ranges = []
for r in rules.values():
    r = list(map(int, r))
    valid_ranges.extend([range(r[0], r[1] + 1), range(r[2], r[3] + 1)])

invalid_sum = 0
for ticket in nearby_tickets:
    for value in list(map(int, ticket.split(','))):
        if not any([value in r for r in valid_ranges]):
            invalid_sum += value

print(invalid_sum)