from comp import Comp
from collections import deque
a = [int(x) for x in open("inputs/d23.txt").read().strip().split(",")]


def solve():
    ans1 = None
    comps = [Comp(a[:]) for _ in range (50)]
    queues = {i: deque() for i in range(50)}
    nat = None
    delivered_by_nat = set()

    # Init computers
    for i in range(50):
        comps[i].add_one_input(i)
        comps[i].run()

    # Run networking
    while True:
        idle = nat and all(not queues[i] for i in range(50))
        if idle:
            X, Y = nat
            if (X,Y) in delivered_by_nat:
                return ans1, Y
            queues[0].extend([X,Y])
            delivered_by_nat.add((X,Y))
        for i in range(50):
            if not queues[i]:
                comps[i].add_one_input(-1)
            else:
                comps[i].add_one_input(queues[i].popleft())
                comps[i].add_one_input(queues[i].popleft())
            comps[i].run()
            try:
                dest, X, Y = [comps[i].get_one_output() for _ in range(3)]
                if dest == 255:
                    if not ans1:
                        ans1 = Y
                    nat = [X, Y]
                else:
                    queues[dest].extend([X,Y])
            except IndexError:
                continue

first, second = solve()
print(first)
print(second)
