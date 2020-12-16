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

valid_ranges = {}
for field, r in rules.items():
    r = list(map(int, r))
    valid_ranges[field] = [range(r[0], r[1] + 1), range(r[2], r[3] + 1)]

valid_tickets = []
for ticket in nearby_tickets:
    valid = True
    ticket = list(map(int, ticket.split(',')))
    for value in ticket:
        if not any([value in r for ranges in valid_ranges.values() for r in ranges]):
            valid = False
    if valid:
        valid_tickets += [ticket]

candidates = {n: list(rules.keys()) for n in range(len(rules.keys()))}

for ticket in valid_tickets:
    for n, value in enumerate(ticket):
        for field, ranges in valid_ranges.items():
            if field in candidates[n] and not any([value in r for r in ranges]):
                candidates[n].remove(field)

while max([len(c) for c in candidates.values()]) > 1:
    unique_fields = [f[0] for f in candidates.values() if len(f) == 1]
    for k, f in candidates.items():
        candidates[k] = [v for v in f if v not in unique_fields or len(f) == 1]

departure_fields = [k for k, v in candidates.items() if 'departure' in v[0]]

product = 1
for v in [int(my_ticket.split(',')[n]) for n in departure_fields]:
    product *= v

print(product)
