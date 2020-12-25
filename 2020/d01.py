from aocd import numbers


def first(goal: int) -> int:
    for i, a in enumerate(numbers):
        for b in numbers[i:]:
            if a + b == goal:
                return a * b


def second(goal: int) -> int:
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers[i:]):
            for c in numbers[j:]:
                if a + b + c == goal:
                    return a * b * c


def main() -> None:
    print("Part 1:", first(goal=2020))
    print("Part 2:", second(goal=2020))


if __name__ == "__main__":
    main()
