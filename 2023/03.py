from itertools import product, takewhile

from helpers import lines

gr = lines("03")
h = len(gr)
w = len(gr[0])
s = set()

a1 = 0
a2 = 0
for y, x in product(range(h), range(w)):
    if not gr[y][x].isdigit() and gr[y][x] != ".":
        f = []
        for j, i in product(range(y - 1, y + 2), range(x - 1, x + 2)):
            if (
                j < 0
                or j >= h
                or i < 0
                or i >= w
                or not gr[j][i].isdigit()
                or (j, i) in s
            ):
                continue
            lh = "".join(
                reversed(list(takewhile(lambda x: x.isdigit(), reversed(gr[j][:i]))))
            )
            rh = "".join(takewhile(lambda x: x.isdigit(), gr[j][i:]))
            for k in range(i - len(lh), i + len(rh)):
                s.add((j, k))
            n = int(f"{lh}{rh}")
            a1 += n
            f.append(n)
        if len(f) == 2:
            a, b = f
            a2 += a * b

print(a1)
print(a2)
