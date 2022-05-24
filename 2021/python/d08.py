from dataclasses import dataclass


@dataclass
class Rule:
    num: int
    pattern_length: int
    is_subset_of: int | None = None
    has_subset: int | None = None


lenToNum = {2: 1, 4: 4, 3: 7, 7: 8}
sum = 0


def normalize(s):
    return "".join(sorted(s))

def check_pattern(rule, pattern):
    if rule.pattern_length == len(pattern):
        if rule.is_subset_of and 
        elif rule.has_subset:
            if normalize(pattern[:rule.pattern_length]) == normalize(pattern[rule.has_subset:]):
                return True
        else:
            return True
    return False


def create_map(patterns):
    left = set(patterns)
    rules = [
        Rule(num=2, pattern_length=5),
        Rule(num=5, pattern_length=5, has_subset=6),
        Rule(num=3, pattern_length=5, is_subset_of=1),
        Rule(num=6, pattern_length=6),
        Rule(num=0, pattern_length=6, is_subset_of=1),
        Rule(num=9, pattern_length=6, is_subset_of=4),
        Rule(num=8, pattern_length=8),
        Rule(num=7, pattern_length=3),
        Rule(num=4, pattern_length=4),
        Rule(num=1, pattern_length=2),
    ]

    while rules and left:
        rule = rules.pop()
        for pattern in left:
            if rule.pattern_length == len(pattern):
                if rule.is_subset_of:






for line in open("inputs/d08.txt"):
    patterns, outputs = [x.strip() for x in line.split("|")]
    patterns = set(normalize(s.strip()) for s in patterns.split())
    print([x for x in create_map(patterns)])
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
