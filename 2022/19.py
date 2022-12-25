import re
from math import prod


def solve(lines, mode="first"):
    ans = []
    l = lines if mode == "first" else lines[:3]
    m = 24 if mode == "first" else 32
    for line in l:
        _, a, b, c, d, e, f = [int(x) for x in re.findall(r"\d+", line)]

        costs = ((a,), (b,), (c, d), (e, f))
        to_rock = [(0,), (0,), (0, 1), (0, 2)]  # cost_to_rock
        states: list[tuple[tuple[int, int, int, int], tuple[int, int, int, int]]] = [
            ((1, 0, 0, 0), (0, 0, 0, 0))
        ]
        for i in range(m):
            new_states = []
            for state in states:
                robots, rocks = state

                for i, cost in enumerate(costs):
                    if all(rocks[to_rock[i][j]] >= c for j, c in enumerate(cost)):
                        new_rocks = list(rocks)
                        for j, c in enumerate(cost):
                            new_rocks[to_rock[i][j]] -= c
                        new_rocks = tuple(a + b for a, b in zip(new_rocks, robots))
                        new_robots = list(robots)
                        new_robots[i] += 1
                        new_robots = tuple(new_robots)
                        new_states.append((new_robots, new_rocks))

                new_states.append((robots, tuple(a + b for a, b in zip(rocks, robots))))

            # prune for hundred best in prio order
            states = sorted(
                new_states,
                key=lambda x: sum(
                    10 ** (2 * i) * (x[0][i] + x[1][i]) for i in range(4)
                ),
                reverse=True,
            )[:500]
        ans.append(max(rocks[3] for _, rocks in states))
    return (
        sum((bp + 1) * t for bp, t in enumerate(ans)) if mode == "first" else prod(ans)
    )


lines = open("inputs/19.txt").read().splitlines()
print("ans1", solve(lines))
print("ans2", solve(lines, "second"))
