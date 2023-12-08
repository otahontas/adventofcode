import math
import re
from functools import reduce

from helpers import lines

inst, _, *grid = lines("08")
m = {
    a: {"L": l, "R": r}
    for a, l, r in ((x for x in re.findall(r"[A-Z]*", g) if x != "") for g in grid)
}

currs = [a for a in m.keys() if a[-1] == "A"]

i = 0
steps = 0
found = {}

while True:
    c = inst[i]
    for j, curr in enumerate(currs):
        currs[j] = m[curr][c]
    steps += 1
    i = (i + 1) % len(inst)
    new_currs = []
    for c in currs:
        if c[-1] == "Z":
            found[c] = steps
        else:
            new_currs.append(c)
    if len(new_currs) == 0:
        break
    currs = new_currs
print(found["ZZZ"], reduce(math.lcm, found.values()))
