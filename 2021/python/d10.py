matches = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomp_points = {")": 1, "]": 2, "}": 3, ">": 4}
ans = 0
autocomp_scores = []
for line in open("inputs/d10.txt"):
    s: list[str] = []
    ok = True
    for char in line.strip():
        if char in "{([<":
            s.append(char)
        else:
            o = s.pop()
            if matches[o] != char:
                ans += points[char]
                ok = False
                break
    if ok:
        sum = 0
        for char in reversed(s):
            sum = 5 * sum + autocomp_points[matches[char]]
        autocomp_scores.append(sum)

print(ans)
print(sorted(autocomp_scores)[len(autocomp_scores) // 2])
