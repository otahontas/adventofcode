from comp import Comp

a = [int(x) for x in open("inputs/d19.txt").read().split(",")]


def solve1():
    n = 50
    ans = 0
    for y in range(n):
        for x in range(n):
            c = Comp(a)
            c.add_one_input(x)
            c.add_one_input(y)
            c.run()
            o = c.get_one_output()
            if o == 1:
                ans += 1
    return ans


def solve2():
    threshold = 100
    upleft_corners = {}
    y = 1200  # guessing that first suitable is after row 1200
    x_start = 0
    while True:
        hits = 0
        last_hit = 0
        x = x_start
        while True:
            c = Comp(a)
            c.add_one_input(x)
            c.add_one_input(y)
            c.run()
            o = c.get_one_output()
            if o == 1:
                if hits == 0:
                    x_start = x
                    possible_corner = y - threshold + 1
                    if (
                        possible_corner in upleft_corners
                        and upleft_corners[possible_corner] == x
                    ):
                        return 10000 * x + possible_corner
                hits += 1
                last_hit = x
            if o == 0 and hits != 0:
                break
            x += 1
        if hits >= threshold:
            upleft_corners[y] = last_hit - threshold + 1
        y += 1


print(solve1())
print(solve2())
