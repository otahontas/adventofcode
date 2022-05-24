from collections import deque

o = {}
inp = open("input.txt").read().strip().splitlines()

o_count = 0
for y in range(len(inp)):
    for x in range(len(inp[y])):
        o[complex(x, y)] = int(inp[y][x])
        o_count += 1

total_flashes = 0

round = 0
while True:
    if round == 100:
        print("Part 01:", total_flashes)
    per_round = 0
    q = deque()
    has_flashed = set()
    for point in o:
        o[point] += 1
        if o[point] > 9:
            per_round += 1
            has_flashed.add(point)
            q.append(point)
    while q:
        p = q.popleft()
        o[p] = 0
        for y in range(-1, 2):
            for x in range(-1, 2):
                np = p + complex(x, y)
                if np not in o or np in has_flashed:
                    continue
                o[np] = o[np] + 1
                if o[np] > 9:
                    per_round += 1
                    has_flashed.add(np)
                    q.append(np)
    total_flashes += per_round
    round += 1
    if per_round == o_count:
        print("Part 02: ", round)
        break
