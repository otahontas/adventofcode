rows = open("inputs/d09.txt").read().strip().split("\n")
map = {
    complex(x, y): int(rows[y][x])
    for y, row in enumerate(rows)
    for x in range(len(row))
}
dirs = [(0 + 1j), (1 + 0j), (0 - 1j), (-1 + 0j)]
sum = 0

for point in map:
    lowpoint = True
    for d in dirs:
        neighbor = point + d
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
                neighbor = p + d
                if neighbor in visited or neighbor not in map or map[neighbor] == 9:
                    continue
                basin += 1
                visited.add(neighbor)
                points.append(neighbor)
        basins.append(basin)

basins = list(reversed(sorted(basins)))
print("Part 2", basins[0] * basins[1] * basins[2])
