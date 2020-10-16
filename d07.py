import itertools
from comp import Comp

a = [int(x) for x in open("inputs/d07.txt").read().strip().split(",")]


def find_max_phases_without_feedback():
    highest_signal = 0
    phases = [0, 1, 2, 3, 4]
    for perm in list(itertools.permutations(phases)):
        prev_output = 0
        for phase in perm:
            c = Comp(a)
            c.add_one_input(phase)
            c.add_one_input(prev_output)
            c.run()
            prev_output = c.get_one_output()
        highest_signal = max(highest_signal, prev_output)
    print(highest_signal)


def find_max_phases_with_feedback():
    highest_signal = 0
    phases = [9, 8, 7, 6, 5]
    for perm in list(itertools.permutations(phases)):
        comps = [Comp(a) for _ in range(5)]
        for i in range(5):
            comps[i].add_one_input(perm[i])
        current_comp = 0
        prev_output = 0
        while True:
            if current_comp == 0 and comps[current_comp].is_halted():
                break
            comps[current_comp].add_one_input(prev_output)
            comps[current_comp].run()
            prev_output = comps[current_comp].get_one_output()
            current_comp = current_comp + 1 if current_comp < 4 else 0
        highest_signal = max(highest_signal, prev_output)
    print(highest_signal)


find_max_phases_without_feedback()
find_max_phases_with_feedback()
