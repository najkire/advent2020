import re
from itertools import product

with open('input.txt', 'r') as input_file:
    program = [line.strip() for line in input_file.readlines()]

def apply_mask(mask, value):
    bin_value = format(int(value), 'b').rjust(36, '0')
    rmask = mask[::-1]
    output = ''.join([rmask[n] if rmask[n] in 'X1' else v for n, v in enumerate(bin_value[::-1])])[::-1]
    return output


values = {}

for line in program:
    if line.startswith('mask'):
        mask = re.search(r'[01X]{36}', line).group()
        continue
    ix, val = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
    ix_value = apply_mask(mask, ix)
    x_ix = [n for n, v in enumerate(ix_value) if v == 'X']
    for p in [list(v) for v in product(('0', '1'), repeat=len(x_ix))]:
        ix_value = ''.join([p.pop() if n in x_ix else v for n, v in enumerate(ix_value)])
        values[ix_value] = int(val)

print(sum(values.values()))
