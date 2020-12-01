from comp import Comp
import collections

a = [int(x) for x in open("inputs/d17.txt").read().split(",")]
grid = []
w = 0
h = 0

def first():
    global grid
    global w
    global h
    c = Comp(a)
    c.run()

    sa = []
    while c.outputs:
        sa.append(chr(c.get_one_output()))
    
    s = "".join(sa)
    grid = s.splitlines()
    grid = grid[:-1]
    
    w = len(grid[0])
    h = len(grid)


    def is_intersection(y, x):
        if y < 1 or x < 1 or y > h - 2 or x > w - 2:
            return False
        if (
            grid[y][x] == "#"
            and grid[y - 1][x] == "#"
            and grid[y + 1][x] == "#"
            and grid[y][x - 1] == "#"
            and grid[y][x + 1] == "#"
        ):
            return True
        return False

    ans = 0
    start = (0, 0)

    for y in range(h):
        for x in range(w):
            if grid[y][x] == "^":
                start = (y, x)
            if is_intersection(y, x):
                ans += y * x
    
    print(ans)
    return start

def second(p):
    dirs = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
    visited = set()

    def is_ok(p, move):
        new_point = (p[0] + dirs[d][0], p[1] + dirs[d][1])
        y = new_point[0]
        x = new_point[1]
        if y < 0 or x < 0 or y > h - 1 or x > w - 1:
            return False
        if grid[y][x] == ".":
            return False
        return True

    def find_next_dir(p):
        for d in dirs:
            y = p[0] + dirs[d][0]
            x = p[1] + dirs[d][1]
            if y < 0 or x < 0 or y > h - 1 or x > w - 1:
                continue
            if grid[y][x] == "#" and (y, x) not in visited:
                return d

    def get_relative_dir(prev_dir, new_dir):
        if prev_dir == "U":
            return "R" if new_dir == "R" else "L"
        if prev_dir == "L":
            return "R" if new_dir == "U" else "L"
        if prev_dir == "D":
            return "R" if new_dir == "L" else "L"
        if prev_dir == "R":
            return "R" if new_dir == "D" else "L"

    path = []
    prev_dir = "U"
    while True:
        d = find_next_dir(p)
        if not d:
            break
        rel_dir = get_relative_dir(prev_dir, d)
        prev_dir = d
        path.append(rel_dir)
        visited.add(p)
        steps = 0
        while is_ok(p, dirs[d]):
            p = (p[0] + dirs[d][0], p[1] + dirs[d][1])
            visited.add(p)
            steps += 1
        path.append(str(steps))

    # Print path
    print(",".join(path))

    # Based on previous print result, check what routines to use. Mine are:
    M = "A,A,B,C,C,A,C,B,C,B"
    A = "L,4,L,4,L,6,R,10,L,6"
    B = "L,12,L,6,R,10,L,6"
    C = "R,8,R,10,L,6"

    a[0] = 2
    c = Comp(a)

    def give_ascii_input(s, c):
        for asc in s:
            c.add_one_input(ord(asc))
        c.add_one_input(10)  # add line break
    give_ascii_input(M, c)
    give_ascii_input(A, c)
    give_ascii_input(B, c)
    give_ascii_input(C, c)
    give_ascii_input("n", c)

    c.run()
    o = c.get_all_outputs()
    for output in o:
        if output > 127:
            print( output)

start = first()
second(start)
