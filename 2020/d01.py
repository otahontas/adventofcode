nums = [int(x) for x in open("inputs/d01.txt").read().strip().split("\n")]


def first():
    goal = 2020
    for i, num1 in enumerate(nums):
        for num2 in nums[i:]:
            if num1 + num2 == goal:
                print(num1 * num2)
                return


def second():
    goal = 2020
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i:]):
            for num3 in nums[j:]:
                if num1 + num2 + num3 == goal:
                    print(num1 * num2 * num3)
                    return


first()
second()
