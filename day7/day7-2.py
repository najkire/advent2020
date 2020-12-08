import re

with open('input.txt', 'r') as input_file:
    rules = [line.strip() for line in input_file.readlines()]

bag_rules = {}
for rule in rules:
    bag, contents = re.match(r'^(.*) bags contain (.*)', rule).groups()

    if 'no other bags' in contents:
        bag_rules[bag] = []
        continue

    bag_rules[bag] = [re.match(r'^ ?(\d)+ (.*) bags?.*', r).groups() for r in contents.split(',')]


class Bag:
    def __init__(self, color):
        self.contents = [(int(n), Bag(c)) for n, c in bag_rules[color]]

    def get_total_bags(self):
        if not self.contents:
            return 0
        return sum([n * b.get_total_bags() + n for n, b in self.contents])


bag = Bag('shiny gold')
print(bag.get_total_bags())
