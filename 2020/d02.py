import re
import collections

lines = open("inputs/d02.txt").read().splitlines()

ans1 = 0
ans2 = 0
for line in lines:
    low, high, char, string = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line).groups()
    low = int(low)
    high = int(high)
    freqs = collections.Counter(string)
    if low <= freqs[char] <= high:
        ans1 += 1
    if (string[low - 1] == char) ^ (string[high - 1] == char):
        ans2 += 1

print(ans1)
print(ans2)
