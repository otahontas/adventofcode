nums = [int(x) for x in "0,13,1,8,6,15".split(",")]

def solve():
    seen = {num: (i + 1, 0) for i, num in enumerate(nums)}
    prev = nums[-1]
    index = len(nums) + 1
    
    while index <= 30000000:
        last_seen, prev = seen[prev]
        try:
            seen[prev] = (index, index - seen[prev][0])
        except KeyError:
            seen[prev] = (index, 0)
        if index == 2020:
            print(prev)
        index += 1
    print(prev)

solve()
