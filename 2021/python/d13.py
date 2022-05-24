from collections import defaultdict, deque, Counter

dots_raw, folds = open("input.txt").read().strip().split("\n\n")

ans = 0

dots = set()

for dot in dots_raw.splitlines():
    x, y = dot.split(",")
    x = int(x)
    y = int(y)
    dots.add((x, y))

for round, fold in enumerate(folds.splitlines()):
    _, along = fold.split("fold along ")
    axis, num = along.split("=")
    num = int(num)
    if axis == "y":
        for i in range(num):
            for dot in list(dots):
                x, y = dot
                if y == num + i + 1:
                    dots.remove(dot)
                    dots.add((x, num - i - 1))
    else:
        for i in range(num):
            for dot in list(dots):
                x, y = dot
                if x == num + i + 1:
                    dots.remove(dot)
                    dots.add((num - i - 1, y))

    if round == 0:
        print("ans1", len(dots))

# print image
max_x = 0
max_y = 0

for dot in dots:
    x, y = dot
    max_x = max(max_x, x)
    max_y = max(max_y, y)


print(max_x, max_y)

for y in range(max_y + 1):
    for x in range(max_x + 1):
        if (x, y) in dots:
            print("#", end="")
        else:
            print(".", end="")
    print()
