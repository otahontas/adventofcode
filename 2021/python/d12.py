from collections import defaultdict, deque, Counter


g = defaultdict(list)

for line in open("inputs/d12.txt").read().splitlines():
    s, d = line.strip().split("-")
    g[s].append(d)
    g[d].append(s)


def first():
    q = deque()
    q.append(("start", set()))

    paths = 0
    while q:
        n, seen = q.popleft()
        if n == "end":
            paths += 1
            continue
        for ne in g[n]:
            if ne == "start":
                continue
            if ne.isupper() or ne not in seen:
                q.append((ne, seen | set([ne])))

    return paths


def second():
    q = deque()
    q.append(("start", {}))

    paths = 0
    while q:
        n, seen = q.popleft()
        if n == "end":
            paths += 1
            continue
        for ne in g[n]:
            if ne == "start":
                continue
            if ne.isupper():
                q.append((ne, seen))
                continue
            if ne in seen:
                if all(s == 1 for s in seen.values()):
                    new_seen = dict(seen)
                    new_seen[ne] = 2
                    q.append((ne, new_seen))
            if ne not in seen:
                new_seen = dict(seen)
                new_seen[ne] = 1
                q.append((ne, new_seen))

    return paths


print("Part 1:", first())
print("Part 2:", second())
