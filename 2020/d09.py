from aocd import numbers


def first(offset: int) -> int:
    n = len(numbers)
    for i in range(offset, n):
        start = i - offset
        stop = i
        sum_found = False
        for k in range(start, stop):
            if sum_found:
                break
            for j in range(k, stop):
                if numbers[k] + numbers[j] == numbers[stop]:
                    sum_found = True
                    break
        if not sum_found:
            return numbers[stop]


def second(invalid: int) -> int:
    n = len(numbers)
    for i in range(n - 1):
        s = [numbers[i], numbers[i + 1]]
        i += 2
        while True:
            if sum(s) == invalid:
                return min(s) + max(s)
            if sum(s) > invalid:
                break
            s.append(numbers[i])
            i += 1


def main() -> None:
    invalid = first(offset=25)
    print("Part 1:", invalid)
    print("Part 2:", second(invalid))


if __name__ == "__main__":
    main()
