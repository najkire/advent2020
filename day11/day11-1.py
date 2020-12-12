with open('input.txt', 'r') as input_file:
    grid = [line.strip() for line in input_file.readlines()]

def get_occupied_seats(grid, x, y):
    seats = ''
    for row in grid[max(0, y - 1):min(y + 2, len(grid))]:
        seats += row[max(0, x - 1):min(x + 2, len(row))]

    return sum(s == '#' for s in seats)

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