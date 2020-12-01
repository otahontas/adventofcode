pattern = [1, 0, -1, 0]
s = open("inputs/d16.txt").read().strip()

def tick(a):
    r = []
    la = len(a)
    for i in range(la):
        res = 0
        p_i = 0
        reps = 0
        j = i
        while j < la:
            res += a[j] * pattern[p_i]
            reps += 1
            if reps == i + 1:
                reps = 0
                p_i = 2 if p_i == 0 else 0
                j += i + 1
            j += 1
        r.append(abs(res) % 10)
    return r

def tick2(a):
    r = []
    s = sum(a)
    for i in a:
        r.append(s % 10)
        s -= i
    return r


def first():
    a = [int(x) for x in s]
    for i in range(100):
        a = tick(a)
    res = [str(x) for x in a[:8]]
    print("".join(res))


def second():
    offset = int(s[:7])
    a = [int(x) for x in s]
    b = a * 10000
    c = b[offset:]
    for i in range(100):
        c = tick2(c)
    res = [str(x) for x in c[:8]]
    print("".join(res))

first()
second()
