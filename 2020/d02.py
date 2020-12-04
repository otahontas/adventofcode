import re
import collections

inp = open("inputs/d02.txt").read().splitlines()

ans1 = 0
ans2 = 0
for line in inp:
    match = re.match(r'(\d+)-(\d+) (.): (.+)', line)
    low, high, char, string = match.groups()
    low = int(low)
    high = int(high)
    freqs = collections.Counter(string)
    if low <= freqs[char] <= high:
        ans1 += 1
    if ((string[low-1] == char and string[high-1] != char) or 
        (string[low-1] != char and string[high-1] == char)):
        ans2 += 1

print(ans1)
print(ans2)
