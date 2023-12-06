import re

from helpers import lines

ns = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
to = {n: i + 1 for i, n in enumerate(ns)}
a1, a2 = 0, 0
for r in (re.findall(rf"(?=(\d|{'|'.join(ns)}))", li) for li in lines("01")):
    d = [int(x) for x in r if x.isdigit()]
    a1 += int(f"{d[0]}{d[-1]}")
    h = r[0] if r[0].isdigit() else to[r[0]]
    t = r[-1] if r[-1].isdigit() else to[r[-1]]
    a2 += int(f"{h}{t}")
print(a1, a2)
