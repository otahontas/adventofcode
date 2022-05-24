from collections import Counter

s, m_r = open("inputs/d14.tx").read().strip().split("\n\n")
s = s.strip()

m = {}
for k in m_r.split("\n"):
    a, b = k.strip().split(" -> ")
    m[a] = b


def solve(rounds):
    ps = Counter()
    for i in range(len(s) - 1):
        t = s[i : i + 2]
        ps[t] += 1
    for i in range(rounds):
        nps = Counter()
        for p, c in ps.items():
            a, b = p
            k = m[p]
            nps[f"{a}{k}"] += c
            nps[f"{k}{b}"] += c
        ps = nps
    ans = Counter()
    for p, c in ps.items():
        a, b = p
        ans[a] += c
    most = ans.most_common(1)[0][1]
    least = ans.most_common()[-1][1]
    return most - least + 1  # last char always there too


print("Part 01", solve(10))
print("Part 02", solve(40))
