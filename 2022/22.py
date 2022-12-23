from collections import defaultdict

import re

# inp = """        ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.

# 10R5L5R10L4R5L5"""

inp = open("inputs/22.txt").read()

grid, guide = inp.split("\n\n")
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
        if char == " ":
            continue
        # side can start with # or .
        if char == "#":
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
        if down_y == y:
            print("went over and back")
            break
        down_val = grid[down_y][x]
        if down_val == ".":
            down = complex(x, down_y)
            map1[point][dirs["D"]] = down
            map1[down][dirs["U"]] = point

# create pt2 map
# in my input sides are on places
#   | 1 | 2
#   | 3 |
# 4 | 5 |
# 6 |   |

# Get correct point right side and dir to continue from there
k = 50  # side len


def get_next_right(point: complex):

    x, y = point.real, point.imag

    ## side 2:
    if y < k and x == 3 * k - 1:
        # land on right side of 5 but other way around:
        # e.g. leave from row 0, land on row 149, leave from row 49, land on row 100
        return complex(2 * k - 1, 3 * k - y - 1), dirs["L"]
    ## side 3:
    elif y < 2 * k and x == 2 * k - 1:
        return complex(2 * k - 1, 3 * k - y - 1), dirs["L"]
    ## side 5:
    ## side 6:
    # sides 1 & 4, continue to right normally
    return complex(x + 1, y), dirs["R"]


map2 = defaultdict(dict)
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == " ":
            continue
        # side can start with # or .
        if char == "#":
            continue
        point = complex(x, y)

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
            # get these from func
            right = complex(right_x, y)
            # so if
            # dir = dirs["U"]
            # with right from 6, we go to lowest row of 5 and continue up
            # and viceversa with down (opposite of up) from 5 and continue left
            # dir = dirs["L"]
            # with right from 2, we go to rightest row of 5 and continue left
            # and viceversa with right (opposite of left) from 5 and continue left
            # so always continue left when coming from other
            dir = dirs["R"]  # something that is returned
            dir_opposite = dir * rotations["L"] ** 2
            map2[point][dirs["R"]] = right, dir
            map2[right][dir_opposite] = point, dirs["L"]

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
            dir = dirs["U"]
            dir_opposite = dir * rotations["L"] ** 2
            map2[point][dirs["D"]] = down, dir
            map2[down][dir_opposite] = point, dirs["U"]

guide = [(int(x), None if k == "" else k) for x, k in re.findall("(\d+)([RL]*)", guide)]


def walk(mode="first"):
    map_to_walk = map1 if mode == "first" else map2
    d = complex(1, 0)
    point = start
    assert point is not None
    for steps, rotation in guide:
        for _ in range(steps):
            if d not in map_to_walk[point]:
                break
            if mode == "first":
                point = map_to_walk[point][d]
            else:
                point, d = map_to_walk[point][d]
        if rotation is None:
            continue
        d *= rotations[rotation]

    # get pos of key
    facing = list(dirs.values()).index(d)
    return int(1000 * (point.imag + 1) + 4 * (point.real + 1) + facing)


# freeze defaultdicts
print("ans1", walk("first"))
print("ans2", walk("second"))
