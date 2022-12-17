import re

lines = [x.strip() for x in open("inputs/15.txt").readlines()]

goal_y = 200000
covered_at_goal_y = set()
sensors_and_cov: list[tuple[tuple[int, int], int]] = []

for line in lines:
    sx, sy, bx, by = [int(x) for x in re.findall(r"-*\d+", line)]
    manhattan = abs(sx - bx) + abs(sy - by)
    sensors_and_cov.append(((sx, sy), manhattan))
    if goal_y < sy - manhattan or goal_y > sy + manhattan + 1:
        continue

    y = goal_y
    y_diff = abs(y - sy)
    for x in range(sx - (manhattan - y_diff), sx + (manhattan - y_diff) + 1):
        if complex(x, y) == complex(bx, by):
            # don't mark beacons
            continue
        covered_at_goal_y.add(x)

max_pos = 4000000
sensors_and_cov.sort()


def in_radar(point: complex, covered: tuple[int, int, int, int]):
    sx, sy, bx, by = covered
    manhattan = abs(sx - bx) + abs(sy - by)
    px, py = point.real, point.imag
    return abs(px - sx) + abs(py - sy) <= manhattan


def line_blocked(y):
    intervals = []
    for (sx, sy), m in sensors_and_cov:
        d = m - abs(y - sy)
        if d < 0:
            # not useful range, skip
            continue
        a = sx - d
        b = sx + d
        intervals.append((a, b))
    intervals.sort()
    reach = [intervals[0][0], intervals[0][1]]  # use list for mutation
    for a, b in intervals[1:]:
        if reach[0] <= a <= reach[1] + 1:
            reach[1] = max(reach[1], b)
        else:
            return False, reach[1] + 1  # x that is free
    return True, None


def solve_2(n):
    for y in range(n):
        blocked, x = line_blocked(y)
        if not blocked:
            assert x is not None
            return x * 4000000 + y


print("Part 1:", len(covered_at_goal_y))
print("Part 2:", solve_2(4000000))
