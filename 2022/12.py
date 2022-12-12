import itertools
import networkx as nx


lines = [list(x.strip()) for x in open("inputs/12.txt").readlines()]

dirs = {
    "U": complex(0, -1),
    "D": complex(0, 1),
    "L": complex(-1, 0),
    "R": complex(1, 0),
}

h = len(lines)
w = len(lines[0])

start = complex(0, 0)
goal = complex(0, 0)
for y, x in itertools.product(range(h), range(w)):
    curr = complex(x, y)
    curr_cont = lines[int(curr.imag)][int(curr.real)]
    if curr_cont == "S":
        start = curr
        lines[int(curr.imag)][int(curr.real)] = "a"
    if curr_cont == "E":
        goal = curr
        lines[int(curr.imag)][int(curr.real)] = "z"

# add points to graph

starts = [start]
G = nx.DiGraph()
for y, x in itertools.product(range(h), range(w)):
    point_id = y * h + x
    curr = complex(x, y)
    for d in dirs.values():
        target = curr + d
        if (
            target.real < 0
            or target.real > w - 1
            or target.imag < 0
            or target.imag > h - 1
        ):
            continue

        curr_cont = lines[int(curr.imag)][int(curr.real)]
        if curr_cont == "a":
            starts.append(curr)
        target_cont = lines[int(target.imag)][int(target.real)]

        G.add_node(curr, val=curr_cont)
        G.add_node(target, val=target_cont)

        if ord(target_cont) - ord(curr_cont) <= 1:
            G.add_edge(curr, target)


# for edge in G.edges():
#     print(
#         f"edge from ({edge[0].real}, {edge[0].imag}) to ({edge[1].real, edge[1].imag})"
#     )
# grid = [["X"] * w for _ in range(h)]
# for i, point in enumerate(nx.shortest_path(G, start, goal)):
#     grid[int(point.imag)][int(point.real)] = str(i)

# print grid

# print("start", start)
# print("goal", goal)
# print("graph len", G.size())
lens = []
for s in starts:
    try:
        lens.append(nx.shortest_path_length(G, s, goal))
    except Exception:
        pass

print("lens", lens)

print("Part 1", lens[0])
print("Part 2", min(lens))
