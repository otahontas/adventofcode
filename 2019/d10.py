import math
from typing import Dict, Tuple


# Init stuff
space = [line.strip("\n") for line in open("inputs/d10.txt")]
w = len(space[0])
h = len(space)
asteroids: Dict[Tuple[int, int], int] = {}


def first():
    for i in range(h):
        for j in range(w):
            if space[i][j] == "#":
                asteroids[(j, i)] = len(asteroids) + 1
    routes = [[0 for x in range(len(asteroids) + 1)] for y in range(len(asteroids) + 1)]
    
    
    def find_matches(x, y):
        """ Finds correct matches """
        v = set()
        orig = asteroids[(x, y)]
        for i in range(y, h):
            for j in range(w):
                # Make sure we go through asteroids on this row on only right side
                # Rest of rows are handled from start to end
                if (i == y and j <= x) or (j, i) in v or space[i][j] == ".":
                    continue
                # Mark that there's connection
                pname = asteroids[(j, i)]
                routes[orig][pname] = 1
                routes[pname][orig] = 1
                # mark all asteroids reachable the same way
                # as visited for next rounds
                a, b = ((j - x), (i - y))
                g = math.gcd(a, b)
                a /= g
                b /= g
                v = mark_as_visited((j, i), v, a, b)
    
    
    def mark_as_visited(p, v, xp, yp):
        x = p[0]
        y = p[1]
        if x < 0 or x > w - 1 or y < 0 or y > h - 1:
            return v
        p = (x + xp, y + yp)
        v.add(p)
        return mark_as_visited(p, v, xp, yp)
    
    for a in asteroids:
        find_matches(a[0], a[1])
    
    sums = [sum(r) for r in routes]
    name = sums.index(max(sums))
    point = [k for (k, v) in asteroids.items() if v == name][0]
    print(max(sums), "at", point)
    return point


def second(point):
    def distance(p):
        return math.sqrt((point[0] - p[0]) ** 2 + (point[1] - p[1]) ** 2)
    
    def dotproduct(v1, v2):
        return sum((a * b) for a, b in zip(v1, v2))
    
    def length(v):
        return math.sqrt(dotproduct(v, v))
    
    def angle(v1, v2):
        return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))
    
    def solve_angle(p):
        if p[0] == point[0]:
            if p[1] < point[1]:
                return 0
            else:
                return math.pi
        base_vector = (0, 3)
        compare_vector = (p[0] - point[0], point[1] - p[1])
        a = angle(base_vector, compare_vector)
        if p[0] < point[0]:
            return 2 * math.pi - a
        else:
            return a
    
    points = []
    
    for i in range(h):
        for j in range(w):
            if space[i][j] == "#":
                if i == point[1] and j == point[0]:
                    continue
                p = (j, i)
                a = solve_angle(p)
                points.append((a, distance(p), p))
    
    
    def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
        return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
    
    
    points.sort()
    prev_angle = 0
    i = 1
    for p in points:
        if i > 1 and isclose(prev_angle, p[0]):
            continue
        if i == 200:
            print(p[2][0] * 100 + p[2][1])
        prev_angle = p[0]
        i += 1

point = first()
second(point)
