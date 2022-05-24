from itertools import combinations
from collections import defaultdict

scanners = open("inputs/d19.txt").read().strip().split("\n\n")

scanner = scanners[0]
positions = scanner.splitlines()[1:]
scanner2 = scanners[1]
positions2 = scanner2.splitlines()[1:]


diffs = {
    (a[0], b[0]): tuple(
        abs(int(t) - int(o)) for t, o in zip(a[1].split(","), b[1].split(","))
    )
    for a, b in combinations(enumerate(positions), 2)
}

for k, v in diffs.items():
    print(k, v)

diffs2 = {
    (a[0], b[0]): tuple(
        abs(int(t) - int(o)) for t, o in zip(a[1].split(","), b[1].split(","))
    )
    for a, b in combinations(enumerate(positions2), 2)
}
print("===")

s = set(tuple(sorted(t)) for t in diffs.values())
s2 = set(tuple(sorted(t)) for t in diffs2.values())

print(len(s & s2))
