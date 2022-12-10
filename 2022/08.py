import itertools

lines = [x.strip() for x in open("inputs/08.txt").readlines()]
dirs = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1)]

ans1 = 0
h, w = len(lines), len(lines[0])
for y, x in itertools.product(range(h), range(w)):
    found = False
    orig = complex(x, y)
    for d in dirs:
        p = complex(x, y)
        if found:
            break
        while True:
            p += d
            if p.real < 0 or p.real > w - 1 or p.imag < 0 or p.imag > h - 1:
                found = True
                ans1 += 1
                break
            if lines[int(p.imag)][int(p.real)] >= lines[int(orig.imag)][int(orig.real)]:
                break

print("ans1", ans1)

ans2 = 0
h, w = len(lines), len(lines[0])
for y, x in itertools.product(range(h), range(w)):
    orig = complex(x, y)
    stuff = []
    for d in dirs:
        a = 0
        p = complex(x, y)
        while True:
            p += d
            if p.real < 0 or p.real > w - 1 or p.imag < 0 or p.imag > h - 1:
                break
            a += 1
            if lines[int(p.imag)][int(p.real)] >= lines[int(orig.imag)][int(orig.real)]:
                break
        stuff.append(a)
    a, b, c, d = stuff
    ans2 = max(ans2, a * b * c * d)


print("ans2", ans2)
