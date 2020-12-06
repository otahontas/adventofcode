groups = [line.strip() for line in open("inputs/d06.txt").read().split("\n\n")]

def first():
    ans = sum(len(set(c for c in group if c.isalpha())) for group in groups)
    print(ans)

def second():
    ans = 0
    for group in groups:
        used = set(c for c in group if c.isalpha())
        for person in group.split("\n"):
            used = used.intersection(set(c for c in person))
        ans += len(used)
    print(ans)


first()
second()
