import re

POLICY_RE = r'^(\d+)-(\d+) ([a-z]): (\w+)'

password_validity = []
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        n_low, n_high, letter, word = re.match(POLICY_RE, line.strip()).groups()
        password_validity += [int(n_low) <= word.count(letter) <= int(n_high)]

print(sum(password_validity))