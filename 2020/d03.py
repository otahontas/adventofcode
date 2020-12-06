grid = open("inputs/d03.txt").read().splitlines()
h = len(grid)
w = len(grid[0])


def travel(add_x,add_y):
    x = 0
    y = 0
    counter = 0
    while True:
        x += add_x
        x %= w
        y += add_y
        if (y >= h):
            break
        if (grid[y][x]  == "#"):
            counter += 1
    return counter


ans1 = travel(3,1)
ans2 = ans1
for rep in [(1,1), (5,1), (7,1), (1,2)]:
    ans2 *= travel(rep[0], rep[1])

print(ans1)
print(ans2)
