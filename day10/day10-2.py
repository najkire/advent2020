from itertools import groupby

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def product(items):
    product = 1
    for item in items:
        product *= item
    return product


with open('input2.txt', 'r') as input_file:
    numbers = [int(line.strip()) for line in input_file.readlines()]

chain = sorted(numbers)
gaps = [chain[0]] + [y - x for x, y in zip(chain, chain[1:])] + [3]

chunks = [(k, len(list(g))) for k, g in groupby(gaps, key=lambda x: x != 3)]
permutations = [fibonacci(v + 2) - 1 for k, v in chunks if k]

print(product(permutations))
