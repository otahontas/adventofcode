import re
from math import prod

from helpers import ints, lines

lim = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
a1, a2 = 0, 0
for g, gs in (li.split(":") for li in lines("02")):
    _id = ints(g)[0]
    ok = True
    m = []
    for c, v in lim.items():
        cs = [int(x) for x in re.findall(rf"(\d+) {c}", gs)]
        m.append(max(cs))
        if any(x > v for x in cs):
            ok = False
    a1 += _id if ok else 0
    a2 += prod(m)
print(a1, a2)
