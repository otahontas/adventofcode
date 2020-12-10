from collections import defaultdict
nums = [int(x) for x in open("inputs/d10.txt").read().splitlines()]
nums.sort()

def first():
    diffs = defaultdict(int)
    prev = 0
    for num in nums:
        diffs[num - prev] += 1
        prev += num - prev
    diffs[3] += 1
    print(diffs[1] * diffs[3])


def second():
    ways = defaultdict(int)
    ways[0] = 1
    for num in [0, *nums]:
        for i in [1,2,3]:
            ways[num + i] += ways[num]
    print(ways[max(ways.keys())])

first()
second()
