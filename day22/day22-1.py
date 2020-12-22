with open('input.txt', 'r') as input_file:
    deck_input = [line.strip() for line in input_file.readlines()]

def get_decks():
    deck = []
    for line in deck_input + ['']:
        if not line:
            yield deck
            deck = []
        try:
            deck += [int(line)]
        except ValueError:
            continue

a, b = get_decks()

while min(len(a), len(b)) > 0:
    c_a = a.pop(0)
    c_b = b.pop(0)

    if c_a > c_b:
        a += sorted([c_a, c_b], reverse=True)
    else:
        b += sorted([c_a, c_b], reverse=True)

score = 0
for n, card in enumerate((a + b)[::-1]):
    score += (n + 1) * card

print(score)
