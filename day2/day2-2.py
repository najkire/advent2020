import re

POLICY_RE = r'^(\d+)-(\d+) ([a-z]): (\w+)'

password_validity = []
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        n_low, n_high, letter, word = re.match(POLICY_RE, line.strip()).groups()
        occurrances = [n + 1 for n in range(len(word)) if word[n] == letter]
        password_validity += [(int(n_low) in occurrances) ^ (int(n_high) in occurrances)]

print(sum(password_validity))