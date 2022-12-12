import re
import math

inps = open("inputs/11.txt").read().split("\n\n")

ms = []
for inp in inps:
    monkey = {}
    lines = inp.split("\n")
    monkey["items"] = [int(x) for x in re.findall(r"\d+", lines[1])]
    _, op = lines[2].strip().split("=")
    monkey["op"] = op.strip()
    monkey["test"] = int(re.findall(r"\d+", lines[3])[0])
    monkey["toMonkey"] = [
        int(re.findall(r"\d+", lines[4])[0]),
        int(re.findall(r"\d+", lines[5])[0]),
    ]
    ms.append(monkey)
modder = math.lcm(*[m["test"] for m in ms])
# print("modder", modder)

times = [0 for _ in range(len(ms))]

# for _ in range(20):
for _ in range(10000):
    for i, mon in enumerate(ms):
        for item in mon["items"]:
            times[i] += 1
            op = mon["op"].replace("old", str(item))
            worry = eval(op) % modder
            # worry //= 3  # comment for pt 1
            if worry % mon["test"] == 0:
                ms[mon["toMonkey"][0]]["items"].append(worry)
            else:
                ms[mon["toMonkey"][1]]["items"].append(worry)
        mon["items"] = []
        ms[i] = mon

so = list(reversed(sorted(times)))
print("ans ", so[0] * so[1])
# """
# Test: divisible by 17
# line     If true: throw to monkey 0
# line     If false: throw to monkey 1
# """"
