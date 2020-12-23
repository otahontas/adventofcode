puzzle_input = "157623984"

cups = [int(x) for x in puzzle_input]

class Node:
    def __init__(self, value, left=None):
        self.value = value
        self.left = left
        self.right = None


def solve(cups, repeat=100):
    n = len(cups) + 1
    nodes = {}

    curr = Node(cups[0])
    nodes[curr.value] = curr
    prev = nodes[curr.value]
    for label in cups[1:]:
        nodes[label] = Node(label, prev)
        prev.right = nodes[label]
        prev = nodes[label]
    prev.right = nodes[curr.value]
    nodes[curr.value].left = prev

    for _ in range(repeat):
        first = curr.right
        second = first.right
        last = second.right
        curr.right = last.right
        curr.right.left = curr
        values = set([first.value, second.value, last.value])
        dest = n - 1 if curr.value == 1 else curr.value - 1
        while dest in values:
            dest = n - 1 if dest == 1 else dest - 1
        dest = nodes[dest]
        last.right = dest.right
        dest.right.left = last
        dest.right = first
        first.left = dest
        curr = curr.right
    
    if repeat > 100:
        return nodes[1].right.value * nodes[1].right.right.value

    curr = nodes[1]
    ans = []
    while (curr := curr.right) != nodes[1]:
        ans.append(str(curr.value))
    return "".join(ans)


def first():
    print(solve(cups))


def second():
    n = len(cups) + 1
    bigger_cups = cups[:]
    bigger_cups.extend(range(n, 10 ** 6 + 1))
    print(solve(bigger_cups, 10 ** 7))


first()
second()
