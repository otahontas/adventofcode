def do_one_round(grid, mode):
    h = len(grid)
    w = len(grid[0])
    state_before_round = set(str(row) for row in grid)
    new_grid = [row[:] for row in grid]

    def move_to_direction(point, direction):
        return tuple(map(sum, zip(point, direction)))

    def is_occupied(point):
        y, x = point
        if y < 0 or y >= h:
            return False
        if x < 0 or x >= w:
            return False
        if grid[y][x] == "#":
            return True
        return False

    def has_occupied_point_in_direction(point, direction):
        while True:
            point = move_to_direction(point, direction)
            y, x = point
            if y < 0 or y >= h:
                return False
            if x < 0 or x >= w:
                return False
            if grid[y][x] == "#":
                return True
            if grid[y][x] == "L":
                return False

    directions = [(-1,0), (-1, 1), (0, 1), (1,1), (1,0), (1,-1), (0, -1), (-1, -1)]
    for y in range(h):
        for x in range(w):
            if grid[y][x] == ".":
                continue
            occupied_count = 0
            point = (y,x)

            for direction in directions:
                if mode == "first":
                    adjacent_point = move_to_direction(point, direction)
                    if is_occupied(adjacent_point):
                        occupied_count += 1
                else:
                    if has_occupied_point_in_direction(point, direction):
                        occupied_count += 1

            if not is_occupied(point) and occupied_count == 0:
                new_grid[y][x] = "#"

            tolerance = 4 if mode == "first" else 5
            if is_occupied(point) and occupied_count >= tolerance:
                new_grid[y][x] = "L"

    state_after_round = set(str(row) for row in new_grid)
    if state_before_round == state_after_round:
        return False, sum([row.count("#") for row in new_grid])
    return True, new_grid

def solve(mode):
    grid = [list(line) for line in open("inputs/d11.txt").read().splitlines()]
    while True:
        did_change, result = do_one_round(grid, mode)
        if not did_change:
            return result
        grid = result

print(solve("first"))
print(solve("second"))
