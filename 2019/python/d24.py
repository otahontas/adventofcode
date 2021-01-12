grid = """..##.
#....
.....
#.#.#
#..#."""

# grid = """....#
# #..#.
# #..##
# ..#..
# #...."""

def first():
    def neighbours(point, state):
        neighbours = 0
        dirs = [(1,0), (-1,0), (0,1), (0, -1)]
        for d in dirs:
            if tuple(map(sum, zip(d, point))) in state:
                neighbours += 1
        return neighbours

    def tick(state):
        new_state = set()
        for y in range(5):
            for x in range(5):
                n = neighbours((y,x), state)
                if ((y,x) in state and n == 1) or ((y,x) not in state and 1 <= n <= 2):
                    new_state.add((y,x))
        return new_state

    state = set((y,x) for y, line in enumerate(grid.splitlines()) for x, ch in
                enumerate(line) if ch == "#")
    seen = set()
    seen.add(str(state))
    while True:
        state = tick(state)
        if str(state) in seen:
            break
        seen.add(str(state))
    rating = sum([2 ** (y * 5 + x) for y,x in state])
    print(rating)

first()
