from collections import Counter

from helpers import ints, lines

c = Counter()
a1 = 0
a2 = 0
for line in lines("04"):
    cd, ns = line.split(":")
    _id = ints(cd)[0]
    b = set.intersection(*(set(ints(x)) for x in ns.split("|")))
    a1 += 2 ** (len(b) - 1) if len(b) > 0 else 0
    am = 1 + c[_id]
    a2 += am
    c += Counter({i: am for i in range(_id + 1, _id + len(b) + 1)})

print(a1)
print(a2)
