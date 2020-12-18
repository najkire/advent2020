import numpy as np
from itertools import permutations

NUM_CYCLES = 6
ix_offsets = [np.array(ix) for ix in set(permutations(4*(-1, 0, 1), 4)) if ix != (0, 0, 0, 0)]
value_map = {'.': False, '#': True}
grid = np.genfromtxt('input.txt', dtype=str, comments=None, delimiter=1)
base_shape = np.array(grid.shape)

fullgrid = np.full(base_shape + 2*NUM_CYCLES, False)
fullgrid = np.stack([np.full(fullgrid.shape, False)] * (2 * NUM_CYCLES + 1))
fullgrid = np.stack([np.full(fullgrid.shape, False)] * (2 * NUM_CYCLES + 1))
fullgrid[NUM_CYCLES,NUM_CYCLES,NUM_CYCLES:NUM_CYCLES+base_shape[0],NUM_CYCLES:NUM_CYCLES+base_shape[1]] = np.vectorize(value_map.get)(grid)

def new_value(value, values):
    num_true = np.sum(values)
    if value and num_true in (2, 3):
        return True
    if not value and num_true == 3:
        return True
    return False


for n in range(NUM_CYCLES):
    newgrid = np.full(fullgrid.shape, False)
    for ix in np.ndindex(fullgrid.shape):
        value = fullgrid[ix]
        values = []
        offsets = [tuple(ix + o) for o in ix_offsets]
        for n_ix in offsets:
            try:
                values += [fullgrid[n_ix]]
            except IndexError:
                pass
        newgrid[ix] = new_value(value, values)

    fullgrid = newgrid

print(np.sum(fullgrid))