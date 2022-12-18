lines = open("inputs/18.txt").read().splitlines()
import itertools
from collections import deque

# lines = """1,1,1
# 2,1,1
# """.splitlines()

# lines = """2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5""".splitlines()

cubes = set()

for line in lines:
    x, y, z = map(int, line.strip().split(","))
    cubes.add((x, y, z))

sides = 0

dirs: list[tuple[int, int, int]] = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]

for cube, dir in itertools.product(cubes, dirs):
    x, y, z = dir
    p = (cube[0] + x, cube[1] + y, cube[2] + z)
    if p not in cubes:
        sides += 1


# PART 2

min_x = min(cubes, key=lambda x: x[0])[0]
min_y = min(cubes, key=lambda x: x[1])[1]
min_z = min(cubes, key=lambda x: x[2])[2]
max_x = max(cubes, key=lambda x: x[0])[0]
max_y = max(cubes, key=lambda x: x[1])[1]
max_z = max(cubes, key=lambda x: x[2])[2]


visited = set()
outside = set()

# mark outside the cube
for x, y, z in itertools.product(
    range(min_y, max_x + 1), range(min_y, max_y + 1), range(min_z, max_z + 1)
):
    if (x, y, z) not in cubes:
        print("x", x, "y", y, "z", z)
        # Run dfs to mark all points outside
        stack = [(x, y, z)]
        while stack:
            p = stack.pop()
            outside.add(p)
            a, b, c = p
            for d in dirs:
                h, j, k = d
                np = (a + h, b + j, c + k)
                e, r, t = np
                if np in outside:  # already visited
                    continue
                if np in cubes:  # in cubes, can't go there
                    continue
                    # too far outside (let there be margin of 1)
                m = 1
                if (
                    e < min_x - m
                    or r < min_y - m
                    or t < min_z - m
                    or e > max_x + m
                    or r > max_y + m
                    or t > max_z + m
                ):
                    continue
                stack.append(np)
        break

# Start bunch dfs to find all inner areas and mark how much sides they have
visited = set()
air_sides_sum = 0

for x, y, z in itertools.product(
    range(min_x, max_x + 1), range(min_y, max_y + 1), range(min_z, max_z + 1)
):
    p = (x, y, z)
    if p not in cubes and p not in outside and p not in visited:
        area = set()
        stack = [p]
        while stack:
            p = stack.pop()
            area.add(p)
            a, b, c = p
            for d in dirs:
                h, j, k = d
                np = (a + h, b + j, c + k)
                e, r, t = np
                if np in cubes or np in area:
                    continue
                stack.append(np)
        air_sides = 0
        for air, dir in itertools.product(area, dirs):
            x, y, z = dir
            p = (air[0] + x, air[1] + y, air[2] + z)
            if p in cubes:
                air_sides += 1
        visited = visited.union(area)
        air_sides_sum += air_sides


print("ans1", sides)
print("ans2", sides - air_sides_sum)
