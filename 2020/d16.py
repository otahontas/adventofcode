import re
from functools import reduce
from collections import defaultdict, Counter

notes = open("inputs/d16.txt").read().strip().split("\n\n")

rules = []
for note in notes[0].strip().splitlines():
    rule, ranges = note.split(": ")
    for low, up in re.findall(r"(\d+)-(\d+)", ranges):
        rules.append((int(low), int(up), rule))

error = 0
non_valid_amount = 0
nearby_tickets = notes[2].splitlines()[1:]
potential = defaultdict(list)

for ticket in nearby_tickets:
    valid = True
    potential_from_ticket = defaultdict(list)
    for field, value in enumerate([int(x) for x in ticket.split(",")]):
        valid_rules = [rule for low, up, rule in rules if low <= value <= up]
        if not valid_rules:
            valid = False
            non_valid_amount += 1
            error += value
            break
        potential_from_ticket[field].extend(valid_rules)
    if valid:
        for field, valid_rules in potential_from_ticket.items():
            potential[field].extend(valid_rules)

valid_amount = len(nearby_tickets) - non_valid_amount
for field, rules in potential.items():
    potential[field] = set(k for k, v in Counter(rules).items() if v == valid_amount)

fields = {}
while potential:
    field_num = next(field for field in potential if len(potential[field]) == 1)
    rule = list(potential[field_num])[0]
    fields[field_num] = rule
    del potential[field_num]
    for field in potential:
        potential[field].remove(rule)

my_ticket_values = notes[1].splitlines()[1].split(",")
values = [
    int(value)
    for field, value in enumerate(my_ticket_values)
    if fields[field].startswith("departure")
]

print(error)
print(reduce(lambda x, y: x * y, values))
