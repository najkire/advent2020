from collections import defaultdict

with open('input.txt', 'r') as input_file:
    input = [line.strip() for line in input_file.readlines()]

def tiles(input):
    tile = []
    for line in input + ['']:
        if 'Tile' in line:
            tile_no = int(line.split()[1].strip(':'))
        elif line:
            tile += [line]            
        elif tile:
            yield tile_no, tile
            tile = []

def get_edges(tile):
    edges = [tile[0]]
    edges += [tile[-1]]
    edges += [''.join([r[0] for r in tile])]
    edges += [''.join([r[-1] for r in tile])]

    edges = edges + [e[::-1] for e in edges]
    return edges

edges = defaultdict(set)
tiles = {n: t for n, t in tiles(input)}
for id, tile in tiles.items():
    for edge in get_edges(tile):
        edges[edge].add(id)

corners = set(list(edge)[0] for edge in edges.values() if len(edge) == 1 and list(edges.values()).count(edge) == 4)

product = 1
for c in corners:
    product *= c
    
print(product)
