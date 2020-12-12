from math import cos, radians, sin

with open('input.txt', 'r') as input_file:
    actions = [line.strip() for line in input_file.readlines()]

def rotate_waypoint(w_x, w_y, r):
    r = radians(r)
    return w_x * cos(r) - w_y * sin(r), w_x * sin(r) + w_y * cos(r)


action_map = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'L': 1,
    'R': -1,
}

x, y = 0, 0
w_x, w_y = 10, 1

for line in actions:
    action, amount = line[0], int(line[1:])
    d_x, d_y, d_r = 0, 0, 0
    d_wx, d_wy = 0, 0

    if action == 'F':
        d_x, d_y = amount * w_x, amount * w_y
    if action in ('N', 'E', 'S', 'W'):
        d_wx, d_wy = tuple(amount * x for x in action_map[action])
    if action in ('L', 'R'):
        w_x, w_y = rotate_waypoint(w_x, w_y, amount * action_map[action])

    x += d_x
    y += d_y
    w_x += d_wx
    w_y += d_wy

print(round(abs(x) + abs(y)))
