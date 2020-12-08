with open('input.txt', 'r') as input_file:
    ops = [line.strip() for line in input_file.readlines()]

flip_map = {'nop': 'jmp', 'jmp': 'nop'}
candidates = [n for n, op in enumerate(ops) if op.split()[0] in flip_map.keys()]

for flip in candidates:
    temp_ops = ops.copy()
    temp_op, val = temp_ops[flip].split()
    temp_ops[flip] = f'{flip_map[temp_op]} {val}'

    acc = 0
    seen = set()
    n = 0
    failed = False

    while n + 1 != len(temp_ops):
        if n in seen:
            failed = True
            break
        seen.add(n)

        try:
            op, val = temp_ops[n].split()
        except:
            continue

        if op == 'nop':
            n += 1
        elif op == 'acc':
            acc += int(val)
            n += 1
        elif op == 'jmp':
            n += int(val)

    if not failed:
        print(acc)
        exit()
