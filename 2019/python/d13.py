from comp import Comp
import time

a = [int(x) for x in open("inputs/d13.txt").read().split(",")]
a[0] = 2
grid = [[0] * 40 for _ in range(25)]
c = Comp(a)


def print_grid(grid):
    for row in grid:
        print("".join([str(x) for x in row]))
    print("")


def count_grid(count_blocks=False):
    ball = (0, 0)
    paddle = (0, 0)
    blocktile_count = 0
    x, y = 0, 0
    i = 0
    score = 0
    while len(c.outputs) > 0:
        output = c.get_one_output()
        if i % 3 == 0:
            x = output
        elif i % 3 == 1:
            y = output
        elif i % 3 == 2:
            if output == 2 and count_blocks:
                blocktile_count += 1
            if x == -1 and y == 0:
                score = output
            else:
                grid[y][x] = output if output != 0 else " "
                if output == 3:
                    paddle = (x, y)
                if output == 4:
                    ball = (x, y)
        i += 1
    if count_blocks:
        print(blocktile_count)
    return (ball, paddle, score)

def first():
    c.run()
    return count_grid(count_blocks=True)

def second(ball, paddle, score):
    final_score = score
    c.restart()
    while not c.is_halted():
        if ball[0] < paddle[0]:
            c.add_one_input(-1)
        elif ball[0] > paddle[0]:
            c.add_one_input(1)
        else:
            c.add_one_input(0)
        c.run()
        ball, paddle, score = count_grid()
        final_score = max(final_score, score)

    print(final_score)


ball, paddle, score = first()
second(ball, paddle, score)
