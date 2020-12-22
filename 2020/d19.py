import re

rules_tmp, received = open("inputs/d19.txt").read().split("\n\n")
rules = {}
for rule in rules_tmp.splitlines():
    k, v = rule.split(": ")
    rules[k] = v[1] if "a" in v or "b" in v else v
mode = "first"


def get_regex(start):
    if mode == "second":
        if start == "8":
            return get_regex("42") + "+"
        if start == "11":
            final_rule = "(?:"
            inner = []
            for i in range(1, 5):
                inner.append(
                    get_regex("42") + f"{{{i}}}" + get_regex("31") + f"{{{i}}}"
                )
            final_rule += "|".join(inner)
            final_rule += ")"
            return final_rule
    rule = rules[start]
    if rule in "ab":
        return rule
    final_rule = "(?:"
    inner = []
    for r in rule.split(" | "):
        inner.append("".join(get_regex(num) for num in re.findall("\d+", r)))
    final_rule += "|".join(inner)
    final_rule += ")"
    return final_rule


def first():
    reg = get_regex("0")
    print(sum(bool(re.fullmatch(reg, r)) for r in received.splitlines()))


def second():
    global mode
    mode = "second"
    reg = get_regex("0")
    print(sum(bool(re.fullmatch(reg, r)) for r in received.splitlines()))


first()
second()
