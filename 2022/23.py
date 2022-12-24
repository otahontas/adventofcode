from collections import defaultdict

rows = open("inputs/23.txt").read().splitlines()

# rows = """.....
# ..##.
# ..#..
# .....
# ..##.
# .....""".splitlines()

# rows = """..............
# ..............
# .......#......
# .....###.#....
# ...#...#.#....
# ....#...##....
# ...#.###......
# ...##.#.##....
# ....#..#......
# ..............
# ..............
# ..............""".splitlines()

s = set()
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if char == "#":
            s.add(complex(x, y))

# 8 adjacent positions
dirs = {
    "northwest": complex(-1, -1),
    "north": complex(0, -1),
    "northeast": complex(1, -1),
    "east": complex(1, 0),
    "southeast": complex(1, 1),
    "south": complex(0, 1),
    "southwest": complex(-1, 1),
    "west": complex(-1, 0),
}


def north(p):
    return not any((p + complex(x, -1)) in s for x in range(-1, 2))


def south(p):
    return not any((p + complex(x, 1)) in s for x in range(-1, 2))


def west(p):
    return not any((p + complex(-1, y)) in s for y in range(-1, 2))


def east(p):
    return not any((p + complex(1, y)) in s for y in range(-1, 2))


def print_grid():
    print("==== STATUS ==== ")
    min_y = int(min(s, key=lambda p: p.imag).imag)
    max_y = int(max(s, key=lambda p: p.imag).imag)
    min_x = int(min(s, key=lambda p: p.real).real)
    max_x = int(max(s, key=lambda p: p.real).real)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            char = "#" if complex(x, y) in s else "."
            print(char, end="")
        print()
    print()


funcs = [north, south, west, east]

i = 1
while True:
    # print_grid()
    ns = set()
    moving_to_point = defaultdict(list)

    for p in s:
        if not any((p + d) in s for d in dirs.values()):
            ns.add(p)
            continue
        d = next((f.__name__ for f in funcs if f(p)), None)
        if d:
            moving_to_point[p + dirs[d]].append(p)
        else:
            ns.add(p)
    for p, ps in moving_to_point.items():
        if len(ps) == 1:
            ns.add(p)
        else:
            for pp in ps:
                ns.add(pp)

    # no movements anymore
    if ns == s:
        print("ans2", i)
        break
    # new set of points
    s = ns
    if i == 10:
        # count non occupied
        min_y = int(min(s, key=lambda p: p.imag).imag)
        max_y = int(max(s, key=lambda p: p.imag).imag)
        min_x = int(min(s, key=lambda p: p.real).real)
        max_x = int(max(s, key=lambda p: p.real).real)

        ss = 0
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if complex(x, y) not in s:
                    ss += 1
        print("ans1", ss)

    # shift funcs
    funcs = [*funcs[1:], funcs[0]]
    i += 1
