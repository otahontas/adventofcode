from collections import defaultdict

import re

grid, guide = open("inputs/22.txt").read().split("\n\n")
grid = grid.split("\n")

rotations = {"L": complex(0, -1), "R": complex(0, 1)}
start = None

dirs = {
    "R": complex(1, 0),
    "D": complex(0, 1),
    "L": complex(-1, 0),
    "U": complex(0, -1),
}

# pad grid with empty space in the end
width = max(len(row) for row in grid)
grid = [row.ljust(width, " ") for row in grid]

# create path 1 map
map1 = defaultdict(dict)
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char in [" ", "#"]:
            continue
        point = complex(x, y)
        start = start or point

        # horizontal movement (check right)
        right_x = x + 1
        while True:
            if right_x >= len(row):
                right_x = 0
            if grid[y][right_x] != " ":
                break
            right_x += 1
        right_val = row[right_x]
        if right_val == ".":
            right = complex(right_x, y)
            map1[point][dirs["R"]] = right
            map1[right][dirs["L"]] = point

        # vertical movement (check down)
        down_y = y + 1
        while True:
            if down_y >= len(grid):
                down_y = 0
            if grid[down_y][x] != " ":
                break
            down_y += 1
        down_val = grid[down_y][x]
        if down_val == ".":
            down = complex(x, down_y)
            map1[point][dirs["D"]] = down
            map1[down][dirs["U"]] = point


# create basic map, structure
# map2[point] = { dir1: [(point, dir)], dir2: [(point, dir)]}
# --> returns all directions from point, new point after stepping to dir and new dir
# after stepping there
map2 = defaultdict(dict)
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char in [" ", "#"]:
            continue
        point = complex(x, y)

        if x < len(row) - 1 and grid[y][x + 1] == ".":
            right = complex(x + 1, y)
            map2[point][dirs["R"]] = right, dirs["R"]
            map2[right][dirs["L"]] = point, dirs["L"]

        # vertical movement (check down)
        if y < len(grid) - 1 and grid[y + 1][x] == ".":
            down = complex(x, y + 1)
            map2[point][dirs["D"]] = down, dirs["D"]
            map2[down][dirs["U"]] = point, dirs["U"]

k = 50  # side len
# stitch sides together.
# in my input sides are:
#   | 1 | 2
#   | 3 |
# 4 | 5 |
# 6 |   |
# where following are already connected
# - 1: RD
# - 2: L
# - 3: UD
# - 4: RD
# - 5: UL
# - 6: U
# Rest are
# - 1U <-> 6L, (50,0)<->(0,150) to (99,0)<->(0,199)
for x in range(k, 2 * k):
    first = complex(x, 0)
    if grid[int(first.imag)][int(first.real)] == "#":
        continue
    dest = complex(0, 2 * k + x)
    if grid[int(dest.imag)][int(dest.real)] == ".":
        map2[first][dirs["U"]] = dest, dirs["R"]
        map2[dest][dirs["L"]] = first, dirs["D"]
# - 1L <-> 4L (flipped), (50,0)<->(0,149) to (50,49)<->(0,100)
for y in range(k):
    first = complex(k, y)
    if grid[int(first.imag)][int(first.real)] == "#":
        continue
    dest = complex(0, 3 * k - 1 - y)
    if grid[int(dest.imag)][int(dest.real)] == ".":
        map2[first][dirs["L"]] = dest, dirs["R"]
        map2[dest][dirs["L"]] = first, dirs["R"]
# # - 2U <-> 6B, (100,0)<->(0,199) to (149,0)<->(49,199)
for x in range(2 * k, 3 * k):
    first = complex(x, 0)
    if grid[int(first.imag)][int(first.real)] == "#":
        continue
    dest = complex(x - 2 * k, 4 * k - 1)
    if grid[int(dest.imag)][int(dest.real)] == ".":
        map2[first][dirs["U"]] = dest, dirs["U"]
        map2[dest][dirs["D"]] = first, dirs["D"]
# # - 2R <-> 5R (flipped), (149,0)<->(99,149) to (149,49)<->(99,100)
for y in range(k):
    first = complex(3 * k - 1, y)
    if grid[int(first.imag)][int(first.real)] == "#":
        continue
    dest = complex(2 * k - 1, 3 * k - 1 - y)
    if grid[int(dest.imag)][int(dest.real)] == ".":
        map2[first][dirs["R"]] = dest, dirs["L"]
        map2[dest][dirs["R"]] = first, dirs["L"]
# # - 2D <-> 3R, (100,49)<->(99,50) to (149,49)<->(99,99)
for x in range(2 * k, 3 * k):
    first = complex(x, k - 1)
    dest = complex(2 * k - 1, k + x - 2 * k)
    if grid[int(dest.imag)][int(dest.real)] == ".":
        map2[first][dirs["D"]] = dest, dirs["L"]
        map2[dest][dirs["R"]] = first, dirs["U"]
# # - 4U <-> 3L, (0,100)<->(50,50) to (49,100)<->(50,99)
for x in range(k):
    first = complex(x, 2 * k)
    if grid[int(first.imag)][int(first.real)] == "#":
        continue
    dest = complex(k, k + x)
    if grid[int(dest.imag)][int(dest.real)] == ".":
        map2[first][dirs["U"]] = dest, dirs["R"]
        map2[dest][dirs["L"]] = first, dirs["D"]
# # - 5D <-> 6R. i.e (50,149)<->(49, 150) to (99,149)<->(49,199)
for x in range(k, 2 * k):
    first = complex(x, 3 * k - 1)
    if grid[int(first.imag)][int(first.real)] == "#":
        continue
    dest = complex(k - 1, 2 * k + x)
    if grid[int(dest.imag)][int(dest.real)] == ".":
        map2[first][dirs["D"]] = dest, dirs["L"]
        map2[dest][dirs["R"]] = first, dirs["U"]


guide = [(int(x), None if k == "" else k) for x, k in re.findall("(\d+)([RL]*)", guide)]

reverse_dirs = {v: k for k, v in dirs.items()}


def walk(mode="first"):
    map_to_walk = map1 if mode == "first" else map2
    d = complex(1, 0)
    point = start
    assert point is not None
    visited = {start: 1}
    counter = 2
    for steps, rotation in guide:
        for _ in range(steps):
            if d not in map_to_walk[point]:
                break
            if mode == "first":
                point = map_to_walk[point][d]
            else:
                point, d = map_to_walk[point][d]
        visited[point] = counter
        counter += 1
        counter %= 10
        if rotation is None:
            continue
        d *= rotations[rotation]

    facing = list(dirs.values()).index(d)
    return int(1000 * (point.imag + 1) + 4 * (point.real + 1) + facing)


print("ans1", walk())
print("ans2", walk("second"))
