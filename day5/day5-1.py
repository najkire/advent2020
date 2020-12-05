ROW_MAP = {'F': '0', 'B': '1'}
COL_MAP = {'L': '0', 'R': '1'}

def decode_string(string, char_map):
    string = ''.join(char_map[c] for c in string)
    return int(string, 2)


with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in  input_file.readlines()]

max_seat_id = 0
for line in lines:
    row = decode_string(line[:7], ROW_MAP)
    col = decode_string(line[7:], COL_MAP)

    max_seat_id = max(max_seat_id, row * 8 + col)

print(max_seat_id)