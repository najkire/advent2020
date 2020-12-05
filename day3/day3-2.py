SLOPES = [(1,1), (3,1), (5,1), (7,1), (1,2)]

with open('input.txt', 'r') as input_file:
    forest = [line.strip() for line in input_file.readlines()]

product = 1

for slope in SLOPES:
    n_x, n_y = slope
    x = 0
    n_trees = 0

    for row in forest[n_y::n_y]:
        x += n_x
        if row[x % len(row)] == '#':
            n_trees += 1

    product *= n_trees

print(product)