TARGET = 1930745883

with open('input.txt', 'r') as input_file:
    numbers = [int(line.strip()) for line in input_file.readlines()]

for l in range(2, len(numbers)):
    for n in range(len(numbers) - l):
        if sum(numbers[n:n + l]) == TARGET:
            print(min(numbers[n:n + l]) + max(numbers[n:n + l]))
            exit()
