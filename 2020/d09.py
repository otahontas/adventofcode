nums = [int(x) for x in open("inputs/d09.txt").read().splitlines()]
offset = 25
n = len(nums)


def first():
    for i in range(offset, n):
        start = i - offset
        stop = i
        sum_found = False
        for k in range(start, stop):
            if sum_found:
                break
            for j in range(k, stop):
                if nums[k] + nums[j] == nums[i]:
                    sum_found = True
                    break
        if not sum_found:
            print(nums[i])
            return nums[i]


def second(invalid):
    found = False
    for i in range(n - 1):
        if found:
            break
        s = [nums[i], nums[i + 1]]
        i += 2
        while True:
            if sum(s) == invalid:
                print(min(s) + max(s))
                found = True
                break
            if sum(s) > invalid:
                break
            s.append(nums[i])
            i += 1


invalid = first()
second(invalid)
