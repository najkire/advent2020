import re

with open('input.txt', 'r') as input_file:
    program = [line.strip() for line in input_file.readlines()]

def apply_mask(mask, value):
    rbin_value = format(int(value), 'b').rjust(36, '0')[::-1]
    rmask = mask[::-1]
    output = ''.join([rmask[n] if rmask[n] in '01' else v for n, v in enumerate(rbin_value)])[::-1]
    return int(output, 2)


values = {}

for line in program:
    if line.startswith('mask'):
        mask = re.search(r'[01X]{36}', line).group()
        continue
    ix, val = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
    values[ix] = apply_mask(mask, val)

print(sum(values.values()))
