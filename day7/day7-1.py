MY_BAG = 'shiny gold'

with open('input.txt', 'r') as input_file:
    rules = [line.strip() for line in input_file.readlines()]

allowed_colors = set()
new_bag_colors = [MY_BAG]
while new_bag_colors:
    current_bag_colors = new_bag_colors
    new_bag_colors = []
    for color in current_bag_colors:
        new_bag_colors += [rule.split('bag')[0].strip() for rule in rules if color in rule.split('contain')[1]]
    allowed_colors.update(new_bag_colors)

print(len(allowed_colors))
