with open('input.txt', 'r') as input_file:
    ops = [line.strip() for line in input_file.readlines()]

acc = 0
seen = set()
n = 0
while n not in seen:
    seen.add(n)
    op, val = ops[n].split()
    if op == 'nop':
        n += 1
    elif op == 'acc':
        acc += int(val)
        n += 1
    elif op == 'jmp':
        n += int(val)

print(acc)
