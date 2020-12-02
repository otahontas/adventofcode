lines = open("inputs/d22.txt").readlines()


def calc_pos(pos, n):
    # Calculate pos based on given original position
    for line in lines:
        command, *args = line.split(" ")
        if command == "deal":
            if args[0] == "into":
                pos = n - pos - 1
            else:
                inc = int(args[2])
                pos = pos * inc % n
        else:
            cut = int(args[0])
            if cut > 0:
                if cut <= pos:
                    pos -= cut
                else:
                    pos = n - cut + pos
            else:
                pos += -cut
                pos %= n
    return pos

def calc_num(pos, n, reps):
    # Calculate num given the goal position
    a, b= 1, 0
    for line in lines:
        command, *args = line.split(" ")
        if command == "deal":
            if args[0] == "into":
                a,b = -a, b-a
            else:
                inc = int(args[2])
                a, b = a * pow(inc, -1, n), b
        else:
            cut = int(args[0])
            a, b = a, b + cut * a
    a %= n
    b %= n
    ans = (pow(a,reps, n) * pos + (1 - pow(a, reps, n)) * pow(1 - a, -1, n) * b) % n
    return ans

lines = open("inputs/d22.txt").readlines()
print(calc_pos(2019,10007))
print(calc_num(2020, 119315717514047, 101741582076661))
