from aocd import numbers
from collections import defaultdict


def first(joltages: list[int]) -> int:
    diffs = defaultdict(int)
    prev = 0
    for joltage in joltages:
        diffs[joltage - prev] += 1
        prev += joltage - prev
    diffs[3] += 1
    return diffs[1] * diffs[3]


def second(joltages: list[int]) -> int:
    ways = defaultdict(int)
    ways[0] = 1
    for joltage in [0, *joltages]:
        for i in [1, 2, 3]:
            ways[joltage + i] += ways[joltage]
    return ways[max(ways.keys())]


def main() -> None:
    joltages = sorted(numbers)
    print("Part 1:", first(joltages=joltages))
    print("Part 2:", second(joltages=joltages))


if __name__ == "__main__":
    main()
