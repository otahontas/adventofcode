def get(x, y, round):
    if (x, y) in img:
        return img[(x, y)]
    if round % 2 == 0:
        return "."
    return "#"


def form(x, y, round):
    n = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            v = get(x + j, y + i, round)
            n.append(v)
    return int("".join(["1" if x == "#" else "0" for x in n]), 2)


def tick(img, bounds, round):
    xl, yl, xu, yu = bounds
    newbounds = (xl - 1, yl - 1, xu + 1, yu + 1)
    xl, yl, xu, yu = newbounds
    new_img = {}
    for y in range(yl, yu):
        for x in range(xl, xu):
            point = (x, y)
            ind_in_map = form(x, y, round)
            new_img[point] = map[ind_in_map]
    return new_img, newbounds


map, ilr = open("inputs/d20.txt").read().strip().split("\n\n")

ill = ilr.split()
img = {}
for y in range(len(ill)):
    for x in range(len(ill[y])):
        img[(x, y)] = ill[y][x]

bounds = (0, 0, len(ill[0]), len(ill))


def print_img(img, bounds):
    xl, yl, xu, yu = bounds
    for y in range(yl, yu):
        for x in range(xl, xu):
            print(img[(x, y)], end="")
        print()


for round in range(50):
    img, bounds = tick(img, bounds, round)
    if round in [1, 49]:
        print(sum([1 for x in img if img[x] == "#"]))
