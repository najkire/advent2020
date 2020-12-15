with open('input.txt', 'r') as input_file:
    _ = input_file.readline()
    bus_ids = input_file.readline().strip().split(',')

bus_ids = {n: int(v) for n, v in enumerate(bus_ids) if v != 'x'}

n = 0
s = 1
for m, bus_id in bus_ids.items():
    while (n + m) % bus_id:
        n += s
    s *= bus_id

print(n)
