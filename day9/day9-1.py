from itertools import permutations

PREAMBLE = 25

with open('input.txt', 'r') as input_file:
    numbers = [int(line.strip()) for line in input_file.readlines()]

for n in range(PREAMBLE, len(numbers) - 1):
    valid = set(sum(p) for p in permutations(numbers[n - PREAMBLE:n], 2))
    if numbers[n] not in valid:
        print(numbers[n])
        exit()
