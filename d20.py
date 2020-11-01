from collections import defaultdict, deque
from queue import PriorityQueue

grid = [list(row) for row in open("inputs/d20.txt").read().splitlines()]


def part1():
    checked = set()
    portals = {}

    # Find all portals
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            p1 = grid[y][x]
            if (x, y) in checked or p1 in "#. ":
                continue
            if grid[y + 1][x].isupper():
                checked.add((x, y + 1))
                p2 = grid[y + 1][x]
                point = (x, y - 1) if y > 0 and grid[y - 1][x] == "." else (x, y + 2)
            else:
                checked.add((x + 1, y))
                p2 = grid[y][x + 1]
                point = (x - 1, y) if x > 0 and grid[y][x - 1] == "." else (x + 2, y)
            if f"{p1}{p2}" == "AA" or f"{p1}{p2}" == "ZZ":
                portals[f"{p1}{p2}"] = point
            else:
                id_suffix = "1" if f"{p1}{p2}1" not in portals else "2"
                portals[f"{p1}{p2}{id_suffix}"] = point
            checked.add((x, y))

    # Add portals to graph by their location
    graph = defaultdict(list)
    for portal in portals:
        if "1" in portal:
            node1 = portal
            node2 = f"{portal[:-1]}2"
            graph[node1].append((node2, 1))
            graph[node2].append((node1, 1))

    portals_by_point = {v: k for k, v in portals.items()}

    def find_reachable_portals(start_id, start):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        visited = set()

        q.append((start, 0))
        visited.add(start)

        while q:
            p, dist = q.popleft()
            for d in dirs:
                x, y = tuple(map(sum, zip(d, p)))
                if (x, y) in visited or grid[y][x] != ".":
                    continue
                visited.add((x, y))
                if (x, y) in portals_by_point:
                    reached_id = portals_by_point[(x, y)]
                    graph[start_id].append((reached_id, dist + 1))
                else:
                    q.append(((x, y), dist + 1))

    for portal in portals:
        find_reachable_portals(portal, portals[portal])

    q = PriorityQueue()
    visited = set()
    dists = defaultdict(lambda: 1000)

    q.put((0, "AA"))
    dists["AA"] = 0

    while not q.empty():
        _, a = q.get()
        if a in visited:
            continue
        visited.add(a)
        for u in graph[a]:
            b = u[0]
            w = u[1]
            if dists[a] + w < dists[b]:
                dists[b] = dists[a] + w
                q.put((dists[b], b))

    return dists["ZZ"]


print(part1())


def part2():
    pass


print(part2())
