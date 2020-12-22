from collections import defaultdict, Counter
from functools import reduce
import re

lines = open("inputs/d21.txt").read().splitlines()
potential = {}
all_foods = []

for line in lines:
    foods, allergens = line.split("contains")
    foods = re.findall(r"(\w+)", foods)
    allergens = re.findall(r"(\w+)", allergens)
    all_foods.extend(foods)
    for allergen in allergens:
        if allergen not in potential:
            potential[allergen] = set(foods)
        else:
            potential[allergen] &= set(foods)

# part 1
allergenic_foods = reduce(lambda x, y: {*x, *y}, potential.values())
print(sum(v for k, v in Counter(all_foods).items() if k not in allergenic_foods))

# part 2
final_allergens = []

while potential:
    allergen = next(k for k, v in potential.items() if len(v) == 1)
    food = list(potential[allergen])[0]
    final_allergens.append((allergen, food))
    for foods in potential.values():
        foods.discard(food)
    del potential[allergen]

print(",".join([food for _, food in sorted(final_allergens)]))
