# pip install portion for interval operations
from functools import reduce

import portion as P

from helpers import ints, lines


def solve(i, ms):
    ok = P.empty()
    for mapping in ms[1:]:
        target, source, rang = ints(mapping)
        change = target - source
        s = P.closedopen(source, source + rang)
        ok |= (i & s).apply(
            lambda x: (x.left, x.lower + change, x.upper + change, x.right)
        )
        i -= s
    return i | ok


pts = lines("05", "\n\n")
ss = ints(pts[0])
i1 = reduce(
    lambda x, y: x | y,
    [P.closedopen(a, a + 1) for a in ss],
)
i2 = reduce(
    lambda x, y: x | y,
    [P.closedopen(a, a + b) for a, b in zip(ss[::2], ss[1::2])],
)
for part in pts[1:]:
    ms = part.splitlines()
    i1, i2 = (solve(i, ms) for i in (i1, i2))
print(i1.lower)
print(i2.lower)
