from collections import defaultdict
from copy import deepcopy

rows = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#""".splitlines()


ways = {
    ">": complex(1, 0),
    "<": complex(-1, 0),
    "v": complex(0, 1),
    "^": complex(0, -1),
}


def solve(rows):
    blizzards = defaultdict(list)
    h = len(rows)
    w = len(rows[0])
    start, end = None, None

    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            p = complex(x, y)
            if y == 0 and char == ".":
                start = p
            elif char in ways.keys():
                blizzards[p].append(ways[char])
            elif y == h - 1 and char == ".":
                end = p

    assert start is not None
    assert end is not None

    blizzards_by_minutes = {0: blizzards}

    def get_blizzard(minutes):
        if minutes in blizzards_by_minutes:
            return blizzards_by_minutes[minutes]
        assert minutes - 1 in blizzards_by_minutes
        prev_blizzards = blizzards_by_minutes[minutes - 1]
        new_blizzards = defaultdict(list)
        for b, dirs in prev_blizzards.items():
            for d in dirs:
                new_b = b + d
                if new_b.real == 0:
                    new_b = complex(w - 2, new_b.imag)
                elif new_b.real == w - 1:
                    new_b = complex(1, new_b.imag)
                elif new_b.imag == 0:
                    new_b = complex(new_b.real, h - 2)
                elif new_b.imag == h - 1:
                    new_b = complex(new_b.real, 1)
                new_blizzards[new_b].append(d)
        blizzards_by_minutes[minutes] = new_blizzards
        return new_blizzards

    def manhattan(p1, p2):
        return abs(p1.real - p2.real) + abs(p1.imag - p2.imag)

    def solve_inner(initial_states, goal):
        states = deepcopy(initial_states)
        while True:
            new_states = set()
            for p, time, dist in states:
                new_blizzards = get_blizzard(time + 1)

                ways_to_move = (
                    ways.values() if p != start else [complex(0, 1)]
                )  # only downwards from start
                for d in ways_to_move:
                    new_d = p + d
                    if new_d == goal:
                        return time + 1  # after this minute we would find this
                    if new_d.real in [0, w - 1] or new_d.imag in [0, h - 1]:
                        # wall cant move there
                        continue
                    if new_d in new_blizzards.keys():
                        # blizzard can't move there
                        continue
                    new_states.add((new_d, time + 1, manhattan(new_d, goal)))
                if p not in new_blizzards.keys():  # we can wait
                    new_states.add((p, time + 1, dist))

            # some heurestics: take only best states by distance
            new_states = sorted(new_states, key=lambda x: x[2])[:750]
            states = new_states

    # part 1
    ans = solve_inner([(start, 0, manhattan(start, end))], end)
    back_to_start = solve_inner([(end, ans, manhattan(end, start))], start)
    ans2 = solve_inner([(start, back_to_start, manhattan(start, end))], end)

    print("part 1", ans)
    print("part 2", ans2)


solve(open("inputs/24.txt").read().splitlines())
