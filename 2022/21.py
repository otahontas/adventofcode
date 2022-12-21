import re

lines = open("inputs/21.txt").read().strip().splitlines()

monkeys = {}
for line in lines:
    monkey, value = line.split(": ")
    monkeys[monkey] = value


def solve(monkey):
    op = monkeys[monkey]
    if not op.isdigit():
        a, b = re.findall(r"\w+", op)
        e, r = solve(a), solve(b)
        return eval(op.replace(a, str(e)).replace(b, str(r)))
    else:
        return int(op)


def solve2():
    op = monkeys["root"]
    a, b = re.findall(r"\w+", op)
    k, l = 1, 10**15

    ## Assert that b is the constant
    monkeys["humn"] = str(k)
    b_res = solve(b)
    monkeys["humn"] = str(l)
    b_res2 = solve(b)
    assert b_res == b_res2

    a_res = solve(a)
    # check which way to compare in binary search
    smaller = a_res < b_res

    # binary search
    while l >= 1:
        while True:
            monkeys["humn"] = str(k + l)
            a_res1 = solve(a)
            monkeys["humn"] = str(k + l + 1)
            a_res2 = solve(a)
            # check if we're in correct direction
            res1 = a_res1 < b_res if smaller else a_res1 > b_res
            res2 = a_res2 >= b_res if smaller else a_res2 <= b_res
            if not res1 < res2:
                break
            k += l
        l //= 2
    return k + 1


print("ans1", solve("root"))
print("ans2", solve2())
