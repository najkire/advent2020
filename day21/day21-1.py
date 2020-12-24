from collections import defaultdict
from itertools import chain

with open('input.txt', 'r') as input_file:
    foods = [line.strip() for line in input_file.readlines()]

ingredient_count = defaultdict(int)
allergen_ingredients = defaultdict(set)

for line in foods:
    ingredient_list, allergen_list = line.split(' (contains ')
    ingredients = ingredient_list.split()
    allergens = [a.strip() for a in allergen_list.strip(')').split(',')]

    for allergen in allergens:
        if not allergen_ingredients[allergen]:
            allergen_ingredients[allergen] = set(ingredients)
        else:
            allergen_ingredients[allergen] = allergen_ingredients[allergen].intersection(set(ingredients))

    for ingredient in ingredients:
        ingredient_count[ingredient] +=1

ingredients_without_allergens = set(ingredient_count.keys()) - set(chain(*allergen_ingredients.values()))
ingredient_sum = 0
for ingredient in ingredients_without_allergens:
    ingredient_sum += ingredient_count[ingredient]

print(ingredient_sum)
