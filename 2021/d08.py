lenToNum = {2: 1, 4: 4, 3: 7, 7: 8}
sum = 0


def normalize(s):
    return "".join(sorted(s))


for line in open("inputs/d08.txt"):
    patterns, outputs = [x.strip() for x in line.split("|")]
    patterns = set(normalize(s.strip()) for s in patterns.split())
    outputs = [normalize(s.strip()) for s in outputs.split()]
    numToPattern = {
        lenToNum[len(x)]: normalize(x) for x in patterns if len(x) in lenToNum
    }
    patterns = patterns.difference(set(numToPattern.values()))
    for pattern in patterns:
        if len(pattern) == 6:
            if set(numToPattern[4]).issubset(set(pattern)):
                numToPattern[9] = normalize(pattern)
            elif set(numToPattern[1]).issubset(set(pattern)):
                numToPattern[0] = normalize(pattern)
            else:
                numToPattern[6] = normalize(pattern)
    patterns = patterns.difference(set(numToPattern.values()))
    for pattern in patterns:
        if set(numToPattern[1]).issubset(set(pattern)):
            numToPattern[3] = normalize(pattern)
        elif set(pattern).issubset(set(numToPattern[6])):
            numToPattern[5] = normalize(pattern)
        else:
            numToPattern[2] = normalize(pattern)
    patternToNum = {v: k for k, v in numToPattern.items()}
    sum += int("".join(str(patternToNum[normalize(s)]) for s in outputs))
print(sum)
