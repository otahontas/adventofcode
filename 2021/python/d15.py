import networkx

lines = open("inputs/d15.txt").read().strip().splitlines()

graph = networkx.DiGraph()

neighbours = [complex(1, 0), complex(0, 1), complex(-1, 0), complex(0, -1)]

for y in range(len(lines)):
    for x in range(len(lines[y])):
        graph.add_node(complex(x, y))

goal = complex(len(lines[0]) - 1, len(lines) - 1)

for y in range(len(lines)):
    for x in range(len(lines[y])):
        for n in neighbours:
            nn = n + complex(x, y)
            nx, ny = nn.real, nn.imag
            if nx < 0 or ny < 0 or nx >= len(lines[0]) or ny >= len(lines):
                continue
            graph.add_edge(
                complex(x, y), complex(nx, ny), weight=int(lines[int(ny)][int(nx)])
            )

print(networkx.dijkstra_path_length(graph, complex(0, 0), goal))

# extend the graph
def get_value(x, y, mult):
    val = int(lines[int(y)][int(x)]) + mult
    return val if val < 10 else val - 9


bigger = networkx.DiGraph()

by = len(lines) * 5
bx = len(lines[0]) * 5

for y in range(by):
    for x in range(bx):
        bigger.add_node(complex(x, y))

goal = complex(bx - 1, by - 1)

for y in range(by):
    for x in range(bx):
        for n in neighbours:
            nn = n + complex(x, y)
            nx, ny = nn.real, nn.imag
            mx = nx // len(lines[0])
            my = ny // len(lines)
            ox = nx % len(lines[0])
            oy = ny % len(lines)
            if nx < 0 or ny < 0 or nx >= bx or ny >= by:
                continue
            bigger.add_edge(
                complex(x, y), complex(nx, ny), weight=get_value(ox, oy, mx + my)
            )

print(networkx.dijkstra_path_length(bigger, complex(0, 0), goal))
