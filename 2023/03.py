from itertools import product, takewhile

from helpers import lines

gr = lines("03")
h, w, s, a1, a2 = len(gr), len(gr[0]), set(), 0, 0
for y, x in product(range(h), range(w)):
    if gr[y][x] == "." or gr[y][x].isdigit():
        continue
    f = []
    for j, i in product(range(y - 1, y + 2), range(x - 1, x + 2)):
        if j < 0 or j >= h or i < 0 or i >= w or not gr[j][i].isdigit() or (j, i) in s:
            continue
        lh = "".join(
            reversed(list(takewhile(lambda x: x.isdigit(), reversed(gr[j][:i]))))
        )
        rh = "".join(takewhile(lambda x: x.isdigit(), gr[j][i:]))
        s |= {(j, k) for k in range(i - len(lh), i + len(rh))}
        f.append(int(f"{lh}{rh}"))
        a1 += f[-1]
    if len(f) != 2:
        continue
    a2 += f[0] * f[1]
print(a1, a2)
