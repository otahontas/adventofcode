from functools import reduce


time, busses = open("inputs/d13.txt").read().splitlines()
time = int(time)
busses = [int(x) if x != "x" else x for x in busses.split(",")]


def first():
    best = min([(((time // x + 1) * x - time), x) for x in busses if x != "x"])
    print(best[0] * best[1])


def second():
    # Chinese remainder code from Rosetta code:
    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a * b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod

    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    n = [x for x in busses if x != "x"]
    a = [x - i for i, x in enumerate(busses) if x != "x"]
    print(chinese_remainder(n, a))


first()
second()
