def check_first(a):
    i = 0
    while a[i] != 99:
        a[a[i + 3]] = (
            a[a[i + 1]] + a[a[i + 2]] if a[i] == 1 else a[a[i + 1]] * a[a[i + 2]]
        )
        i += 4
    return a[0]


def find_solution(a, solution):
    for i in range(100):
        for j in range(100):
            a[1] = i
            a[2] = j
            if check_first(a[:]) == solution:
                return 100 * i + j


a = [int(x) for x in open("inputs/d02.txt").read().strip().split(",")]
a[1] = 12
a[2] = 2
print(check_first(a[:]))
print(find_solution(a, 19690720))
