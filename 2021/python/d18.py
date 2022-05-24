import ast
import re
import functools
import itertools
import math

inp = open("inputs/d18.txt").read().strip().splitlines()


def solve(lines):
    path_to_prev = []
    right_from_explode = None
    has_exploded = False
    has_split = False

    def set_val(path, val):
        functools.reduce(list.__getitem__, path[:-1], curr)[path[-1]] = val

    def add_val(path, val):
        functools.reduce(list.__getitem__, path[:-1], curr)[path[-1]] += val

    def explode(a, path=None, path_of_prev=None):
        path = path or []
        nonlocal path_to_prev
        nonlocal right_from_explode
        nonlocal has_exploded
        if isinstance(a, list):
            if len(path) == 4 and not has_exploded:
                if path_to_prev:
                    add_val(path_to_prev, a[0])
                set_val(path, 0)
                right_from_explode = a[1]
                has_exploded = True
            else:
                for i, x in enumerate(a):
                    explode(x, path + [i], path_of_prev)
        else:
            if right_from_explode is not None:
                add_val(path, right_from_explode)
                right_from_explode = None
            path_to_prev = path

    def split(a, path=None):
        nonlocal has_split
        path = path or []
        if has_split:
            return
        if isinstance(a, list):
            for i, x in enumerate(a):
                split(x, path + [i])
        else:
            if not has_split and a >= 10:
                left, right = math.floor(a / 2), math.ceil(a / 2)
                set_val(path, [left, right])
                has_split = True

    curr = ast.literal_eval(lines[0])

    for line in lines[1:]:
        other = ast.literal_eval(line)
        curr = [curr, other]
        while True:
            explode(curr)
            path_to_prev = []
            if has_exploded:
                has_exploded = False
                right_from_explode = None
                continue
            split(curr)
            if has_split:
                has_split = False
                continue
            break

    def sum(a):
        if isinstance(a, list):
            return 3 * sum(a[0]) + 2 * sum(a[1])
        return a

    magnitude = sum(curr)
    return magnitude


print("part 01", solve(inp))

best = 0
for a, b in itertools.combinations(inp, 2):
    res = solve([a, b])
    best = max(best, res)
print("part 02", best)
