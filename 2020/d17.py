from copy import deepcopy

input_grid = [list(x) for x in open("inputs/d17.txt").read().splitlines()]


def solve(mode):
    n = 26

    def create_grid():
        base = n // 2
        grid = []
        if mode == "first":
            for i in range(n + 1):
                grid.append([[0] * (n + 1) for _ in range(n + 1)])

            for x in range(len(input_grid)):
                for z in range(len(input_grid[0])):
                    if input_grid[x][z] == "#":
                        grid[base][base + x][base + z] = 1
        else:
            for i in range(n + 1):
                row = []
                for j in range(n + 1):
                    row.append([[0] * (n + 1) for _ in range(n + 1)])
                grid.append(row)

            for x in range(len(input_grid)):
                for z in range(len(input_grid[0])):
                    if input_grid[x][z] == "#":
                        grid[base][base][base + x][base + z] = 1
        return grid

    def active_neighbours(grid, i, j, k, l=None):
        active = 0
        for y in range(i - 1, i + 2):
            for x in range(j - 1, j + 2):
                for z in range(k - 1, k + 2):
                    if mode == "first":
                        if (y, x, z) == (i, j, k):
                            continue
                        if grid[y][x][z] == 1:
                            active += 1
                    else:
                        for w in range(l - 1, l + 2):
                            if (y, x, z, w) == (i, j, k, l):
                                continue
                            if grid[y][x][z][w] == 1:
                                active += 1
        return active

    def do_cycle(grid):
        active_count = 0
        new_grid = deepcopy(grid)
        for y in range(1, n):
            for x in range(1, n):
                for z in range(1, n):
                    if mode == "first":
                        active = active_neighbours(grid, y, x, z)
                        if (
                            grid[y][x][z] == 1
                            and 2 <= active <= 3
                            or grid[y][x][z] == 0
                            and active == 3
                        ):
                            new_grid[y][x][z] = 1
                            active_count += 1
                        else:
                            new_grid[y][x][z] = 0
                    else:
                        for w in range(1, n):
                            active = active_neighbours(grid, y, x, z, w)
                            if (
                                grid[y][x][z][w] == 1
                                and 2 <= active <= 3
                                or grid[y][x][z][w] == 0
                                and active == 3
                            ):
                                new_grid[y][x][z][w] = 1
                                active_count += 1
                            else:
                                new_grid[y][x][z][w] = 0
        return new_grid, active_count

    new_grid = create_grid()
    for r in range(6):
        new_grid, active_count = do_cycle(new_grid)

    print(active_count)


solve("first")
solve("second")
