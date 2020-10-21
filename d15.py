from comp import Comp
import pickle
from collections import deque

a = [int(x) for x in open("inputs/d15.txt").read().split(",")]
n = 48

grid = [[" "] * n for _ in range(n)]

dirs = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
marks = {0: "#", 1: ".", 2: "X"}
solution_1 = 0
solution_1x = 0
solution_1y = 0
first_solved = True  # check this to False if grid should be formed again


def move(y, x, c, d):
    c.add_one_input(d)
    c.run()
    o = c.get_one_output()
    m = marks[o]
    grid[y + dirs[d][0]][x + dirs[d][1]] = m
    return (c, o)


def solve(y, x, tape, steps):
    ok = []
    for pd in range(1, 5):
        py = y + dirs[pd][0]
        px = x + dirs[pd][1]
        if grid[py][px] != " ":
            continue
        (c, o) = move(y, x, Comp(tape), pd)
        if o == 0:
            continue
        if o == 2:
            global solution_1
            global solution_1y
            global solution_1x
            solution_1 = steps + 1
            solution_1y = py
            solution_1x = px
        ok.append((c.tape[:], (py, px), steps + 1))
    return ok


def first():
    y = n // 2
    x = n // 2
    grid[y][x] = "."
    oks = [(a[:], (y, x), 0)]

    while True:
        next_oks = []
        for ok in oks:
            y = ok[1][0]
            x = ok[1][1]
            tape = ok[0]
            steps = ok[2]
            ret_ok = solve(y, x, tape, steps)
            next_oks.extend(ret_ok)
        oks = next_oks
        if not oks:
            break


filename = "d15_pickled_grid.p"  # for pickling

# First
if not first_solved:
    first()
    print("steps", solution_1)
    print(f"oxygen system at {solution_1x}, {solution_1y}")
    # save grid
    with open(filename, "wb") as f:
        pickle.dump(grid, f)

# Second
# reload pickled array
maze = []
with open(filename, "rb") as f:
    maze = pickle.load(f)

for row in maze:
    print("".join(row))

# run bfs
start = (42, 42)
dist = [[0] * n for _ in range(n)]
dirs = list(dirs.values())

visited = set()
q = deque()
q.append(start)

max_dist = 0

while q:
    n = q.popleft()
    visited.add(n)

    for d in dirs:
        y = n[0] + d[0]
        x = n[1] + d[1]
        if maze[y][x] == "." and (y, x) not in visited:
            q.append((y, x))
            dist[y][x] = dist[n[0]][n[1]] + 1
            max_dist = max(dist[y][x], max_dist)

print(max_dist)
