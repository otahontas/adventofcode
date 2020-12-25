from aocd import lines


def travel(slope: tuple[int, int], grid: list[str]) -> int:
    x, y, counter = 0, 0, 0
    height, width = len(grid), len(grid[0])
    right, down = slope

    while True:
        x = (x + right) % width
        y += down
        if y >= height:
            break
        if grid[y][x] == "#":
            counter += 1

    return counter


def main() -> None:
    ans = travel(slope=(3, 1), grid=lines)
    print("Part 1:", ans)

    for slope in [(1, 1), (5, 1), (7, 1), (1, 2)]:
        ans *= travel(slope=slope, grid=lines)
    print("Part 2:", ans)


if __name__ == "__main__":
    main()
