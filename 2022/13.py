import functools

lines = [x.strip() for x in open("inputs/13.txt").read().split("\n\n")]


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        # print("comparing ints", a, b)
        return a <= b
    if isinstance(a, int) and isinstance(b, list):
        # print("converting for comparison int and lsit", a, b)
        return compare([a], b)
    if isinstance(a, list) and isinstance(b, int):
        # print("converting for comparison list and int", a, b)
        return compare(a, [b])

    # second round maybe?
    if isinstance(a, list) and isinstance(b, list):
        # print("comparing list and list", a, b)
        if len(a) == 0 and len(b) == 0:
            return True
        if len(a) > 0 and len(b) == 0:
            return False
        if len(a) == 0 and len(b) > 0:
            return True
        head_a, *tail_a = a
        head_b, *tail_b = b
        if head_a == head_b:
            return compare(tail_a, tail_b)
        return compare(head_a, head_b)

    raise Exception(f"Invalid input {a} & {b}A")


def bubble(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if not compare(arr[j], arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return


def compare_for_sort(a, b):
    if compare(a, b):
        return -1
    return 1


indices = []
dividends = [[[2]], [[6]]]
packets = [*dividends]
for i, line in enumerate(lines):
    a_raw, b_raw = [x.strip() for x in line.split("\n")]
    a = eval(a_raw)
    b = eval(b_raw)
    packets.append(a)
    packets.append(b)
    if compare(a, b):
        indices.append(i + 1)

bubble(packets)

print("ans1", sum(indices))
[x, y] = [packets.index(x) + 1 for x in dividends]
print("ans2", x * y)
