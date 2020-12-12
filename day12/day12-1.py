from math import cos, radians, sin

with open('input.txt', 'r') as input_file:
    actions = [line.strip() for line in input_file.readlines()]

def get_cartesian(r, amount):
    deg = radians(r % 360)
    return amount * cos(deg), amount * sin(deg)

action_map = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'L': 1,
    'R': -1,
}

r, x, y = 0, 0, 0

for line in actions:
    action, amount = line[0], int(line[1:])
    d_x, d_y, d_r = 0, 0, 0

    if action == 'F':
        d_x, d_y = get_cartesian(r, amount)
    if action in ('N', 'E', 'S', 'W'):
        d_x, d_y = tuple(amount * x for x in action_map[action])
    if action in ('L', 'R'):
        d_r = amount * action_map[action]

    x += d_x
    y += d_y
    r += d_r

print(abs(x) + abs(y))
