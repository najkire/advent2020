TARGET = 1930745883

with open('input.txt', 'r') as input_file:
    numbers = [int(line.strip()) for line in input_file.readlines()]

for l in range(2, len(numbers)):
    for n in range(len(numbers) - l):
        crange = numbers[n:n + l]
        if sum(crange) == TARGET:
            print(min(crange) + max(crange))
            exit()
