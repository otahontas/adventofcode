a = [int(x) for x in open("inputs/d01.txt").read().strip().split("\n")]

def first():
    print(sum([x // 3 - 2 for x in a]))

def second():
    f = lambda x, s=0: s if x < 6 else f(x // 3 - 2, s + x // 3 - 2)
    print(sum(list(map(f, a))))

first()
second()
