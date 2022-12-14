import itertools

lines = open("inputs/14.txt").readlines()

rocks = set()

# e.g. lowest_point
highest_y = 0

for line in lines:
    splits_raw = line.strip().split(" -> ")
    splits = []
    for split in splits_raw:
        a, b = split.split(",")
        splits.append((int(a), int(b)))
    for i in range(len(splits) - 1):
        a = splits[i]
        b = splits[i + 1]
        if a > b:
            a, b = b, a
        start, end = a, b
        for y, x in itertools.product(
            range(start[1], end[1] + 1), range(start[0], end[0] + 1)
        ):
            highest_y = max(y, highest_y)
            rocks.add(complex(x, y))

sands = set()
sand_start = complex(500, 0)
floor_y = highest_y + 2
while True:
    sand = sand_start
    ans_found = False
    while True:
        down = sand + complex(0, 1)
        if down not in rocks and down not in sands and down.imag < floor_y:
            # print("going down")
            sand = down
            continue
        left_down = sand + complex(-1, 1)
        if left_down not in rocks and left_down not in sands and down.imag < floor_y:
            # print("going left down")
            sand = left_down
            continue
        right_down = sand + complex(1, 1)
        if right_down not in rocks and right_down not in sands and down.imag < floor_y:
            # print("going right down")
            sand = right_down
            continue

        # at rest
        sands.add(sand)
        if sand == sand_start:
            ans_found = True
        break
    if ans_found:
        break

print("ans1", len(sands))
