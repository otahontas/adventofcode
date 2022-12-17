import math

rocks_raw = [
    x.strip().split("\n")
    for x in """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split(
        "\n\n"
    )
]
rocks = []
for rock in rocks_raw:
    r = []
    for y in range(len(rock)):
        r.extend(complex(x, y) for x in range(len(rock[y])) if rock[y][x] == "#")
    rocks.append(r)


pattern = open("inputs/17.txt").read().strip()
highest_y = 1  # take into account that floor is 0, so highest is under floor
highest_y_2nd_part = 1  # take into account that floor is 0, so highest is under floor
offset_2nd_part = 0
width = 7
taken = set()

prev_highest_y = 0
prev_highest_rock = 0
n = 1000000000000
# n = 100000

pattern_i = 0
i = 0
while i <= n:
    if i == 2022:
        print("part 1:", int(-highest_y + 1))

    rel_rock = rocks[i % len(rocks)]
    # point is top left corner
    top_left = complex(2, highest_y - max(x.imag for x in rel_rock) - 1 - 3)
    abs_rock = [x + top_left for x in rel_rock]

    while True:
        jet = pattern[pattern_i % len(pattern)]
        pattern_i += 1

        if pattern_i % len(pattern) == 0:
            # addofset for skipping rounds in pt. 2
            if pattern_i >= 2 * len(pattern):
                highest_diff = prev_highest_y - highest_y
                rounds_diff = i - prev_highest_rock
                rounds_to_skip = (n - i) // rounds_diff
                offset_2nd_part = rounds_to_skip * highest_diff
                i += rounds_to_skip * rounds_diff
            prev_highest_y = highest_y
            prev_highest_rock = i
        if jet == "<":
            potential_abs_rock = [x + complex(-1, 0) for x in abs_rock]
            # check if blocked, if not set abs rock
            if (
                all(x not in taken for x in potential_abs_rock)
                and min(x.real for x in potential_abs_rock) >= 0
            ):
                abs_rock = potential_abs_rock
        elif jet == ">":
            potential_abs_rock = [x + complex(1, 0) for x in abs_rock]
            # check if blocked, if not set abs rock
            if (
                all(x not in taken for x in potential_abs_rock)
                and max(x.real for x in potential_abs_rock) <= width - 1
            ):
                abs_rock = potential_abs_rock
        # try to move downwards
        potential_abs_rock = [x + complex(0, 1) for x in abs_rock]
        if (
            any(x in taken for x in potential_abs_rock)
            or max(x.imag for x in potential_abs_rock) > 0
        ):
            # can't move anymore, so landing
            for r in abs_rock:
                taken.add(r)
            highest_y = min(highest_y, min(x.imag for x in abs_rock))
            highest_y_2nd_part = highest_y - offset_2nd_part
            break
        # can move, set to new point
        abs_rock = potential_abs_rock
    i += 1
print("part 2:", int(-highest_y_2nd_part))
