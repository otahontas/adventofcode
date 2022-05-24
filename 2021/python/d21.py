import itertools
import re
from dataclasses import dataclass


@dataclass
class Player:
    id: int
    space: int
    score: int = 0


lines = open("inputs/d21.txt").read().splitlines()

players = [
    Player(id=(x[0]), space=int(x[1]))
    for x in [re.findall("\d+", line) for line in lines]
]


# rolls = 0
# dice = itertools.cycle(range(1, 101))
# for in_turn in itertools.cycle(players):
#     rolls += 3
#     results = in_turn.space = (
#         in_turn.space - 1 + sum(itertools.islice(dice, 3))
#     ) % 10 + 1
#     in_turn.score += in_turn.space
#     if in_turn.score >= 1000:
#         other = next(x for x in players if x.id != in_turn.id)
#         print("Part 1:", rolls * other.score)
#         break

s = []
