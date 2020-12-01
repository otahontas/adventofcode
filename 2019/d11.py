from comp import Comp
import numpy as np

n = 90


a = [int(x) for x in open("inputs/d11.txt").read().split(",")]


def paint(start_from_white = False):
    x = n // 2 
    y = n // 2
    grid = [["."] * n for _ in range(n)]
    c = Comp(a)
    d = "U"
    colored = set()
    if start_from_white:
        grid[y][x] = "#"

    while not c.is_halted():
        inp = 0 if grid[y][x] == "." else 1
        c.add_one_input(inp)
        c.run()

        # Paint
        color = "." if c.get_one_output() == 0 else "#"
        grid[y][x] = color
        colored.add((y, x))

        # Turn
        if d == "U":
            d = "L" if c.get_one_output() == 0 else "R"
        elif d == "R":
            d = "U" if c.get_one_output() == 0 else "D"
        elif d == "D":
            d = "R" if c.get_one_output() == 0 else "L"
        elif d == "L":
            d = "D" if c.get_one_output() == 0 else "U"
        else:
            print("something not right)")
            break

        # Move
        if d == "U":
            y += 1
        elif d == "R":
            x += 1
        elif d == "D":
            y -= 1
        elif d == "L":
            x -= 1
        else:
            print("something not right)")
            break


    if start_from_white:
        A = np.asanyarray(grid)
        B= np.flipud(A)
        for row in B:
            print("".join(row))
    else:
        print(len(colored))


paint()
paint(start_from_white=True)
