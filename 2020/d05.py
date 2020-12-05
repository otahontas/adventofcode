import re

lines=open("inputs/d05.txt").read().splitlines()

replace = {ord(k): ord(v) for (k,v) in {"F": "0", "B": "1", "L": "0", "R": "1"}.items()}
ids = set()
for line in lines:
    line = line.translate(replace)
    ids.add(int(line, 2))

seat = 0
while seat in ids or seat+1 not in ids or seat-1 not in ids:
    seat += 1

print(max(ids))
print(seat)
