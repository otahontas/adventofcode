test1 = [
    int(x)
    for x in """1
2
-3
3
-2
0
4""".splitlines()
]
test2 = [
    int(x)
    for x in """16
-12
78
4444
0
2""".splitlines()
]
nums = [int(x) for x in open("inputs/20.txt").read().splitlines()]


class Node:
    def __init__(self, value):
        self.value = value
        self.moves = value
        self.left = None
        self.right = None


def print_list(node):
    start = node
    curr = node
    while curr.right != start:
        print(curr.value, end=" ")
        curr = curr.right
    print(curr.value, end=" ")
    print("")


decryption_key = 811589153


def solve(nums, mode="first"):
    nodes = []
    node_zero = None

    for num in nums:
        node = Node(num)
        if num == 0:
            node_zero = node
        nodes.append(node)
        if len(nodes) > 1:
            prev = nodes[-2]
            prev.right = node
            node.left = prev
    nodes[0].left = nodes[-1]
    nodes[-1].right = nodes[0]

    assert node_zero is not None
    for node in nodes:
        if mode == "second":
            node.moves *= decryption_key
        node.moves %= len(nodes) - 1

    rounds = 1 if mode == "first" else 10

    for _ in range(rounds):
        for node in nodes:
            for _ in range(node.moves):
                toMove = node.right
                toMove.left = node.left
                toMove.left.right = toMove
                node.left = toMove
                node.right = toMove.right
                toMove.right = node
                node.right.left = node

    poss = [1000, 2000, 3000]
    s = 0
    for pos in poss:
        cur = node_zero
        for _ in range(pos % len(nodes)):
            cur = cur.right
        if mode == "second":
            print("pos", pos, "value", cur.value)
        s += cur.value if mode == "first" else cur.value * decryption_key
    return s


assert solve(test1) == 3
assert solve(test1, "second") == 1623178306
assert solve(test2) == 4446
ans1 = solve(nums)
ans2 = solve(nums, "second")
assert ans1 == 7278
print("Part 1:", ans1)
print("Part 2:", ans2)
