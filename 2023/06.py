from math import ceil, floor, prod, sqrt

from helpers import ints, lines


def solve(t, r):
    rt = (t + sqrt((-t) ** 2 - 4 * r)) / 2
    return floor(rt) - ceil(t - rt) + 1


ts, rs = (list(ints(li)) for li in lines("06"))
t, r = [int("".join(str(x) for x in nums)) for nums in [ts, rs]]
print(prod(solve(t, r) for t, r in zip(ts, rs)), solve(t, r))
