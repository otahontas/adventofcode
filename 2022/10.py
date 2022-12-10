lines = [x.strip() for x in open("inputs/10.txt").readlines()]

it = iter(lines)
X = 1
sprite = {0, 1, 2}
cycle_to_take_cmd = 1
cmd = "noop"
signal_strs = []
crt_line = 0

for cycle in range(1, 241):  # running against 240 cycles
    # run result from prev cmd and schedule new one
    if cycle == cycle_to_take_cmd:
        if cmd.startswith("addx"):
            _, b = cmd.split(" ")
            X += int(b)
            sprite = {X - 1, X, X + 1}
        try:
            cmd = next(it)
        except StopIteration:
            break
        cycles_to_run = 1 if cmd.startswith("noop") else 2
        cycle_to_take_cmd = cycle + cycles_to_run

    if cycle == 20 or cycle % 40 == 20:
        signal_strs.append(cycle * X)
    char_to_print = "#" if cycle - (40 * crt_line) - 1 in sprite else "."

    print(char_to_print, end="")
    if cycle % 40 == 0:
        crt_line += 1
        print("")

print("ans1", sum(signal_strs))
