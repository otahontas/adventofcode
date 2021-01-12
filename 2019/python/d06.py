def create_graph(a):
    g = {}
    for pair in a:
        n1, n2 = pair.split(")")
        if n1 not in g:
            g[n1] = []
        if n2 not in g:
            g[n2] = []
        g[n1].append(n2)
        g[n2].append(n1)
    return g


def find_paths(g):
    directs = 0
    indirects = 0
    v = set()
    q = []
    q.append(("COM", 0))

    while q:
        n, l = q.pop(0)
        if n in g:
            for ne in g[n]:
                if ne not in v:
                    directs += 1
                    indirects += l
                    v.add(ne)
                    q.append((ne, l + 1))
    return directs + indirects - 2


def find_shortest(g):
    v = set()
    q = []
    q.append(("YOU", 0))

    while q:
        n, l = q.pop()
        if n in g:
            for ne in g[n]:
                if ne == "SAN":
                    return l - 1
                if ne not in v:
                    v.add(ne)
                    q.append((ne, l + 1))


a = open("inputs/d06.txt").read().strip().split("\n")
g = create_graph(a)
print(find_paths(g))
print(find_shortest(g))
