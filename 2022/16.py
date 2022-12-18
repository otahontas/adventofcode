import re
from copy import deepcopy

import networkx as nx

# brrr

lines = open("inputs/16_example.txt").read().splitlines()
G = nx.Graph()
for line in lines:
    valve, *neighbors = re.findall("[A-Z]{2}", line)
    flow_rate = int(re.findall("\d+", line)[0])
    G.add_node(valve, flow_rate=flow_rate)
    G.add_edges_from([(valve, neighbor) for neighbor in neighbors])

fw = nx.floyd_warshall(G)
cache = {}


def create_key(node, not_visited, minutes):
    key = node
    for n in sorted(not_visited):
        key += n
    key += str(minutes)
    return hash(key)


# calculate all the paths
def search(node, not_visited, minutes):
    key = create_key(node, not_visited, minutes)
    if key in cache:
        return cache[key]

    ress = []
    for other in not_visited:
        fr = G.nodes[other]["flow_rate"]
        dist = fw[node][other]
        if dist >= minutes:  # can't make it in time
            continue
        new_not_visited = deepcopy(not_visited)
        new_not_visited.remove(other)
        new_minutes = minutes - dist - 1  # min to open
        res = fr * new_minutes + search(
            other, new_not_visited, minutes - fw[node][other] - 1
        )
        ress.append(res)
    result = max(ress, default=0)
    cache[key] = result
    return result


with_flow_rates = set(filter(lambda n: G.nodes[n]["flow_rate"] > 0, G.nodes))

first = search("AA", with_flow_rates, 30)
print("first", first)
