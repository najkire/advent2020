SUM = 2020

with open('input.txt', 'r') as input_file:
    numbers = [int(n.strip()) for n in input_file.readlines()]

while numbers:
    num = numbers.pop(0)
    target = SUM - num
    if target in numbers:
        print(f'{num} * {target} = {num * target}')
        exit()