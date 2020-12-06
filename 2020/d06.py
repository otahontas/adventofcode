lines = [line.strip() for line in open("inputs/d06.txt").read().split("\n\n")]

def first():
    ans = 0
    for line in lines:
        ans += len(set(c for c in line if c.isalpha()))
    print(ans)

def second():
    ans = 0
    for line in lines:
        used = set(c for c in line.strip("\n") if c.isalpha())
        for subgroup in line.split("\n"):
            used = used.intersection(set(c for c in subgroup if c.isalpha()))
        ans += len(used)
    print(ans)


first()
second()
