def run(a, inp):
    i = 0
    while True:
        o = []
        b = str(a[i])[::-1]
        for p in range(5):
            try:
                o.append(int(b[p]))
            except IndexError:
                o.append(0)
        opcode = (str(o[0])+str(o[1]))[::-1]

        if opcode == '99':
            return

        if opcode == '03' or opcode == '04':
            if opcode == '03':
                a[a[i+1]] = inp
            else:
                v = a[a[i+1]] if o[2] == 0 else a[i+1]
                print(v)
            i += 2
            continue

        p1 = a[a[i+1]] if o[2] == 0 else a[i+1]
        p2 = a[a[i+2]] if o[3] == 0 else a[i+2]
        if opcode == '05':
            i = p2 if p1 != 0 else i + 3
            continue

        if opcode == '06':
            i = p2 if p1 == 0 else i + 3
            continue

        if opcode == '01':
            a[a[i+3]] = p1 + p2
        elif opcode == '02':
            a[a[i+3]] = p1 * p2
        elif opcode == '07':
            a[a[i+3]] = 1 if p1 < p2 else 0
        elif opcode == '08':
            a[a[i+3]] = 1 if p1 == p2 else 0
        i += 4

a = [int(x) for x in open('d05.txt').read().strip().split(',')]
# first
run(a[:],1)
# second
run(a[:],5)
