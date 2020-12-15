N_STOP = 30000000

with open('input.txt', 'r') as input_file:
    numbers = [int(n) for n in input_file.readline().strip().split(',')]

last_loc = {v: n for n, v in enumerate(numbers[:-1])}
last_number = numbers[-1]
i = len(numbers)
while i < N_STOP:
    try:
        last_index = last_loc[last_number]
        number = i - last_index - 1
    except KeyError:
        number = 0
    last_loc[last_number] = i - 1
    last_number = number
    i += 1

print(last_number)