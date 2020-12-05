with open('input.txt', 'r') as input_file:
    forest = [line.strip() for line in input_file.readlines()]

n_trees = 0
x = 0

for row in forest[1:]:
    x += 3
    if row[x % len(row)] == '#':
        n_trees += 1

print(n_trees)