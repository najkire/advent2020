ROW_MAP = {'F': '0', 'B': '1'}
COL_MAP = {'L': '0', 'R': '1'}

def decode_string(string, char_map):
    string = ''.join(char_map[c] for c in string)
    return int(string, 2)


with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in  input_file.readlines()]

seat_ids = set()
for line in lines:
    row = decode_string(line[:7], ROW_MAP)
    col = decode_string(line[7:], COL_MAP)

    seat_ids.add(row * 8 + col)

my_seat_id = [i for i in range(max(seat_ids)) if not (i in seat_ids) and set([i - 1, i + 1]).issubset(seat_ids)]
print(my_seat_id)