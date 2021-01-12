from comp import Comp

a = [int(x) for x in open("inputs/d21.txt").read().split(",")]

def solve(code):
    c = Comp(a);
    for i in code:
        for j in [ord(c) for c in i]:
            c.add_one_input(j)
        c.add_one_input(10)
    c.run()
    o = c.get_all_outputs()
    for output in o:
        if output <= 127:
            print(chr(output), end="")
        else:
            print("ans:", output)

# 1 Jump only if there's hole in A,B,C, but D is ground
rules_1 = ["NOT A J", "NOT B T", "OR T J", "NOT C T", "OR T J", "AND D J"]
solve([*rules_1, "WALK"])

# 2 Jump only if first is true and also E or H is ground
rules_2 = ["NOT E T", "NOT T T", "OR H T", "AND T J"]
solve([*rules_1, *rules_2, "RUN"])
