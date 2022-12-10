lines = [x.strip() for x in open("inputs/09.txt").readlines()]

dirs = {
    "U": complex(0, -1),
    "D": complex(0, 1),
    "L": complex(-1, 0),
    "R": complex(1, 0),
}


def solve(length: int):
    h = complex(0, 0)
    t: list[complex] = []
    for _ in range(length - 1):
        t.append(complex(0, 0))

    def dist(p1, p2):
        return p1 - p2

    visited = set()

    for line in lines:
        a, b = line.split(" ")
        for _ in range(int(b)):
            h += dirs[a]
            prev = h
            for i, curr in enumerate(t):
                d = dist(prev, curr)
                if abs(d.imag) > 1 or abs(d.real) > 1:
                    dx = (
                        0
                        if curr.real == prev.real
                        else (1 if prev.real > curr.real else -1)
                    )
                    dy = (
                        0
                        if curr.imag == prev.imag
                        else (1 if prev.imag > curr.imag else -1)
                    )
                    curr += complex(dx, dy)
                prev = curr
                t[i] = curr
                if curr == t[-1]:
                    visited.add(curr)

    return len(visited)


print("ans1", solve(2))
print("ans2", solve(10))
