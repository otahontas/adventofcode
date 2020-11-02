from collections import defaultdict
from itertools import combinations
from queue import PriorityQueue

grid = open("inputs/d18_2.txt").read().splitlines()
maze = {}
keys = {}
doors = {}
graph = defaultdict(list)


def construct_maze_keys_and_doors():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            char = grid[y][x]
            maze[(x, y)] = char
            if char in "#.":
                continue
            if char == "@" or char.islower():
                keys[char] = (x, y)
            else:
                doors[char] = (x, y)


def find_path_between_keys(a, b):
    def process(point):
        if point not in visited and maze[point] not in "#":
            new_path = path.copy()
            new_path.append(point)
            q.put((steps + 1, new_path))

    q = PriorityQueue()
    steps = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    q.put((steps, [a]))
    visited = set()
    while q:
        steps, path = q.get()
        last = path[-1]
        visited.add(last)
        if last == b:
            return steps, path
        for d in dirs:
            process(tuple(map(sum, zip(last, d))))


def construct_graph():
    for a, b in combinations(sorted(keys.keys()), 2):
        steps, path = find_path_between_keys(keys[a], keys[b])
        if not any(maze[x].islower() or maze[x] == "@" for x in path[1:-1]):
            needed_keys = frozenset([k.lower() for k, v in doors.items() if v in path])
            graph[a].append((steps, b, needed_keys))
            graph[b].append((steps, a, needed_keys))


# part 1
construct_maze_keys_and_doors()
construct_graph()
paths = PriorityQueue()
paths.put((0, "@", frozenset("@")))
fastest = defaultdict(int)

while paths:
    steps, node, collected = paths.get()
    if collected == keys.keys():
        print(steps)
        break
    for dist, adj_node, req in graph[node]:
        if req <= collected:
            new_collected = collected | frozenset([adj_node])
            total = steps + dist
            best = fastest[(adj_node, new_collected)]
            if not best or total < best:
                fastest[(adj_node, new_collected)] = total
                paths.put((total, adj_node, new_collected))

# part 2
