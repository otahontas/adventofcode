cals = [x.strip() for x in open("inputs/d01.txt").read().split("\n\n")]
sums = []


desc = list(
    reversed(sorted(sum((int(num) for num in nums.split("\n"))) for nums in cals))
)

print(f"1: {max(desc)}")
print(f"2: {sum(desc[:3])}")
