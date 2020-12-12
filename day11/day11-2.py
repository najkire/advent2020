with open('input.txt', 'r') as input_file:
    grid = [line.strip() for line in input_file.readlines()]

def vertical(grid, x, y):
    col = ''.join([r[x] for r in grid])
    return col[:y][::-1], col[y + 1:]

def horizontal(grid, x, y):
    row = grid[y]
    return row[:x][::-1], row[x + 1:]

def diagonal(grid, x, y):
    diag = ''.join([r[n - y + x] for n, r in enumerate(grid) if 0 <= n - y + x < len(r)])
    return diag[:min(x, y)][::-1], diag[min(x, y) + 1:]

def reverse_diagonal(grid, x, y):
    rdiag = ''.join([r[::-1][len(r) - 1 + n - y - x] for n, r in enumerate(grid) if 0 <= len(r) - 1 + n - y - x < len(r)])
    return rdiag[:min(len(grid[0]) - 1 - x, y)][::-1], rdiag[min(len(grid[0]) - 1 - x, y) + 1:]

def get_occupied_seats(grid, x, y):
    directions = [
        vertical,
        horizontal,
        diagonal,
        reverse_diagonal,
    ]
    views = []
    for d in directions:
        views.extend(d(grid, x, y))
    is_free = [True for d in views if ('#' not in d) or ('L' in d and d.index('L') < d.index('#'))]
    return 8 - sum(is_free)

def sweep_grid(grid):
    new_grid = []
    for y, row in enumerate(grid):
        new_row = ''
        for x, seat in enumerate(row):
            occupied_seats = get_occupied_seats(grid, x, y)
            if seat == 'L' and not occupied_seats:
                new_row += '#'
                continue
            if seat == '#' and occupied_seats > 4:
                new_row += 'L'
                continue
            new_row += seat
        new_grid += [new_row]
    return new_grid


while True:
    new_grid = sweep_grid(grid)
    if grid == new_grid:
        break
    grid = new_grid

print(sum(s == '#' for s in ''.join(grid)))