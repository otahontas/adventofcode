inp = [int(x) for x in open("inputs/d01.txt").read().strip().split("\n")]

def solve1():
    goal = 2020
    for i, num1 in enumerate(inp):
        for num2 in inp[i:]:
            if num1 + num2 == goal:
                print(num1 * num2)
                return

def solve2():
    goal = 2020
    for i, num1 in enumerate(inp):
        for j, num2 in enumerate(inp[i:]):
            for num3 in inp[j:]:
                if num1 + num2 + num3 == goal:
                    print(num1 * num2 * num3)
                    return
solve1()
solve2()
