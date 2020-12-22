import re

lines = open("inputs/d18.txt").read().strip().splitlines()


def solve(mode):
    regexes = (
        ["\(\d+ [\*|\+] \d+\)", "\d+ [\*|\+] \d+"]
        if mode == "first"
        else ["\(\d+ \+ \d+\)", "\d+ \+ \d+", "\(\d+ \* \d+\)", "\d+ \* \d+"]
    )
    nums = []
    for line in lines:
        while True:
            matched = False
            for regex in regexes:
                match = re.search(regex, line)
                if match:
                    matched = True
                    res = str(eval(match.group(0)))
                    line = re.sub(regex, res, line, 1)
                    break
            if not matched:
                nums.append(int(line))
                break
    print(sum(nums))


solve("first")
solve("second")
