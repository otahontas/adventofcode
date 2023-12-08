from helpers import lines
from collections import Counter as C
from dataclasses import dataclass

s = [
    lambda h: len(set(h)) == 1,
    lambda h: C(h).most_common(1)[0][1] == 4,
    (lambda h: C(h).most_common()[0][1] == 3 and C(h).most_common()[1][1] == 2),
    lambda h: C(h).most_common()[0][1] == 3,
    (lambda h: C(h).most_common()[0][1] == 2 and C(h).most_common()[1][1] == 2),
    lambda h: C(h).most_common()[0][1] == 2,
    lambda h: len(set(h)) == 5,
]
g = lambda h: next((i for i, f in enumerate(s) if f(h)), 0)


@dataclass
class H:
    t: int
    h: str
    b: int
    o: list[str]

    def __lt__(self, other):
        return (
            next(
                (
                    self.o.index(x) < self.o.index(y)
                    for x, y in zip(self.h, other.h)
                    if x != y
                ),
                False,
            )
            if self.t == other.t
            else self.t < other.t
        )


def solve(lis, pt2=False):
    ob = ["A", "K", "Q", "J", "T", *(str(x) for x in reversed(range(2, 10)))]
    o = [*[x for x in ob if x != "J"], "J"] if pt2 else ob
    hs = []
    for li in lis:
        h, b = li.split(" ")
        if pt2:
            k = "A" if set(h) == {"J"} else C(h).most_common()[0][0]
            k = C(h).most_common()[1][0] if k == "J" else k
            i = g(h.replace("J", k))
        else:
            i = g(h)
        hs.append(H(i, h, int(b), o))
    return sum(h.b * (i + 1) for i, h in enumerate(reversed(sorted(hs))))


print(solve(lines("07")), solve(lines("07"), True))
