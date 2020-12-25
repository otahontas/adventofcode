from aocd import lines


def main() -> None:
    source, dest = "FBLR", "0101"
    seat_ids = {int(line.translate(line.maketrans(source, dest)), 2) for line in lines}
    print("Part 1:", max(seat_ids))

    seat = 0
    while seat in seat_ids or seat + 1 not in seat_ids or seat - 1 not in seat_ids:
        seat += 1
    print("Part 2", seat)


if __name__ == "__main__":
    main()
