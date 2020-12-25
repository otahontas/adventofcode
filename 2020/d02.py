import re
from aocd import lines
from collections import Counter


def main() -> None:
    first, second = 0, 0

    for line in lines:
        low, high, char, string = re.match(
            r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line
        ).groups()
        low, high = int(low), int(high)
        if low <= Counter(string)[char] <= high:
            first += 1
        if (string[low - 1] == char) ^ (string[high - 1] == char):
            second += 1
    print("Part 1:", first)
    print("Part 2:", second)


if __name__ == "__main__":
    main()
