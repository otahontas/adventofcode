import re
import collections

lines = [x.strip() for x in open("inputs/d07.txt").read().splitlines()]

bags = collections.defaultdict(lambda: {})
for line in lines:
    container, content_as_list = line.split(" bags contain ")
    contents = re.findall(r"(\d+) ([\w\s]+(?= ))", content_as_list)
    for amount, bag_name in contents:
        bags[container][bag_name] = int(amount)


def dfs1(bag):
    if bag == "shiny gold":
        return True
    if bag not in bags:
        return False
    has_gold = False
    for inner in bags[bag]:
        has_gold |= dfs1(inner)
    return has_gold


def dfs2(bag, amount):
    if bag not in bags:
        return amount
    new = 0 if bag == "shiny gold" else amount
    for content, num in bags[bag].items():
        new += dfs2(content, num * amount)
    return new


print(sum([dfs1(bag) for bag in bags.keys() if bag != "shiny gold"]))
print(dfs2("shiny gold", 1))
