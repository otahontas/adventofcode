from dataclasses import dataclass
from typing import List, Tuple
import re


@dataclass
class Comp:

    tape: List[Tuple[str, int]]
    accumulator: int = 0
    head: int = 0

    def run(self):
        seen = set()
        terminated = False
        while self.head not in seen:
            seen.add(self.head)
            try:
                op, arg = self.tape[self.head]
            except IndexError:
                terminated = True
                break
            if op == "acc":
                self.accumulator += arg
                self.head += 1
            elif op == "jmp":
                self.head += arg
            elif op == "nop":
                self.head += 1
        if terminated:
            print(self.accumulator)


instructions = re.findall(r"(\w+) ([\+-]\d+)", open("inputs/d08.txt").read())


def first():
    tape = [(op, int(arg)) for op, arg in instructions]
    c = Comp(tape)
    c.run()
    print(c.accumulator)


def second():
    tape = [(op, int(arg)) for op, arg in instructions]
    for i, inst in enumerate(tape):
        new_tape = tape[:]
        op, arg = inst
        new_tape[i] = ("jmp", arg) if op == "nop" else new_tape[i]
        new_tape[i] = ("nop", arg) if op == "jmp" else new_tape[i]
        c = Comp(new_tape)
        c.run()


first()
second()
