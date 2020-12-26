import re
from aocd import data
from dataclasses import dataclass
from typing import Optional

Tape = list[tuple[str, int]]


@dataclass
class Comp:
    tape: Tape
    accumulator: int = 0
    head: int = 0

    def run(self, mode: str = "first") -> Optional[int]:
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
        if terminated or mode == "first":
            return self.accumulator


def first(tape: Tape) -> int:
    c = Comp(tape)
    return c.run()


def second(tape: Tape) -> int:
    for i, instruction in enumerate(tape):
        new_tape = tape[:]
        op, arg = instruction
        new_tape[i] = ("jmp", arg) if op == "nop" else new_tape[i]
        new_tape[i] = ("nop", arg) if op == "jmp" else new_tape[i]
        c = Comp(new_tape)
        value = c.run(mode="second")
        if value:
            return value


def main() -> None:
    instructions = re.findall(r"(\w+) ([\+-]\d+)", data)
    tape = [(op, int(arg)) for op, arg in instructions]
    print("Part 1:", first(tape[:]))
    print("Part 2:", second(tape[:]))


if __name__ == "__main__":
    main()
