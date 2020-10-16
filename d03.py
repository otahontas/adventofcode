def get_points(w):
    x = 0
    y = 0
    steps = 0
    points = {}
    dirs = {"D": (0, -1), "U": (0, 1), "L": (-1, 0), "R": (1, 0)}
    for p in w:
        d = p[0]
        for _ in range(int(p[1:])):
            x += dirs[d][0]
            y += dirs[d][1]
            steps += 1
            points[(x, y)] = steps
    return points


fw, sw, last = open("inputs/d03.txt").read().split("\n")
fw, sw = [x.split(",") for x in [fw, sw]]

fw_points = get_points(fw)
sw_points = get_points(sw)

steps = []
common = set()
for pair in fw_points:
    if pair in sw_points:
        common.add((abs(pair[0]), abs(pair[1])))
        steps.append(fw_points[pair] + sw_points[pair])

print(min([sum(x) for x in common]))
print(min(steps))
