import re

# TODO: write this with fp-ts at some point

raw_stacks, raw_lines = list(open("inputs/05.txt").read().split("\n\n"))
lines = raw_lines.strip().split("\n")
stack_lines = raw_stacks.split("\n")

stack_nums = [int(x) for x in re.findall("\\d+", stack_lines[-1])]

stacks: list[list[str]] = [[] for _ in range(len(stack_nums))]
stacks2: list[list[str]] = [[] for _ in range(len(stack_nums))]
for line in stack_lines[:-1]:
    for i, char in enumerate(line[1::4]):
        stacks[i].append(char)
        stacks2[i].append(char)
for i in range(len(stacks)):
    stacks[i] = list(reversed(list(filter(lambda x: x != " ", stacks[i]))))
    stacks2[i] = list(reversed(list(filter(lambda x: x != " ", stacks2[i]))))

for line in lines:
    a, b, c = [int(x) for x in re.findall("\\d+", line)]
    l = [stacks[b - 1].pop() for _ in range(a)]
    l2 = list(reversed([stacks2[b - 1].pop() for _ in range(a)]))
    stacks[c - 1] += l
    stacks2[c - 1] += l2

s1 = "".join(stack[-1] for stack in stacks)
print("ans1", s1)
s2 = "".join(stack[-1] for stack in stacks2)
print("asn2", s2)
