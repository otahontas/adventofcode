from collections import defaultdict

map = {}
inp = [row for row in open("inputs/d09.txt").read().strip().split("\n")]

for y in range(len(inp)):
    for x in range(len(inp[y])):
        map[(x, y)] = int(inp[y][x])


def s(p, o):
    return (p[0] + o[0], p[1] + o[1])


sum = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for point in map:
    lowpoint = True
    for d in dirs:
        neighbor = s(point, d)
        if neighbor not in map:
            continue
        if map[neighbor] <= map[point]:
            lowpoint = False
    if lowpoint:
        sum += map[point] + 1

print("Part 1", sum)

visited = set()
basins = []
for point in map:
    if map[point] != 9 and point not in visited:
        basin = 1
        points = [point]
        visited.add(point)
        while points:
            p = points.pop()
            for d in dirs:
                neighbor = s(p, d)
                if neighbor in visited or neighbor not in map or map[neighbor] == 9:
                    continue
                basin += 1
                visited.add(neighbor)
                points.append(neighbor)
        basins.append(basin)

basins = list(reversed(sorted(basins)))
print("Part 2", basins[0] * basins[1] * basins[2])
