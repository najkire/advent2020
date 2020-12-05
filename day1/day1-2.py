SUM = 2020

with open('input.txt', 'r') as input_file:
    numbers = [int(n.strip()) for n in input_file.readlines()]

while numbers:
    num = numbers.pop(0)
    n_temp = numbers.copy()
    target = SUM - num
    while n_temp:
        num2 = n_temp.pop(0)
        target2 = target - num2
        if target2 in n_temp:
            print(f'{num} * {num2} * {target2} = {num * num2 * target2}')
            exit()
