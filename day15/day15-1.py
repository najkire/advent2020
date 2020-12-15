N_STOP = 2020

with open('input.txt', 'r') as input_file:
    numbers = [int(n) for n in input_file.readline().strip().split(',')]

while len(numbers) < N_STOP:
    if numbers[-1] not in numbers[:-1]:
        numbers += [0]
        continue
    last_index = len(numbers) - numbers[:-1][::-1].index(numbers[-1]) - 1
    numbers += [len(numbers) - last_index]

print(numbers[-1])