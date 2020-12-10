with open('input.txt', 'r') as input_file:
    numbers = [int(line.strip()) for line in input_file.readlines()]

chain = sorted(numbers)
gaps = [chain[0]] + [y - x for x, y in zip(chain, chain[1:])] + [3]

print(gaps.count(1) * gaps.count(3))
