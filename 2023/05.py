# pip install portion for interval operations
from functools import reduce

import portion as P

from helpers import ints, lines


def solve(i, ms):
    ok = P.empty()
    for t, s, r in (ints(m) for m in ms[1:]):
        c = t - s
        s = P.closedopen(s, s + r)
        ok |= (i & s).apply(lambda x: (x.left, x.lower + c, x.upper + c, x.right))
        i -= s
    return i | ok


pts = lines("05", "\n\n")
ss = ints(pts[0])
a1, a2 = reduce(
    lambda x, ms: (solve(x[0], ms), solve(x[1], ms)),
    (pt.splitlines() for pt in pts[1:]),
    (
        reduce(
            lambda x, y: x | y,
            (P.closedopen(a, a + 1) for a in ss),
        ),
        reduce(
            lambda x, y: x | y,
            (P.closedopen(a, a + b) for a, b in zip(ss[::2], ss[1::2])),
        ),
    ),
)
print(a1.lower, a2.lower)
