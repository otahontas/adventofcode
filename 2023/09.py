from helpers import lines, ints

s1, s2 = 0, 0
for li in lines("09"):
    nums = [ints(li)]
    while True:
        nums.append([b - a for a, b in zip(nums[-1][:-1], nums[-1][1:])])
        if all(x == 0 for x in nums[-1]):
            break
    for i in range(len(nums) - 2, -1, -1):
        nums[i] = [nums[i][0] - nums[i + 1][0], *nums[i], nums[i][-1] + nums[i + 1][-1]]
    s1 += nums[0][-1]
    s2 += nums[0][0]
print(s1, s2)
