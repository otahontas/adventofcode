import itertools

inputs = []


def run(a,i=0):
    output = 0
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
            inputs.append(output)
            return (a,99)

        if opcode == '03' or opcode == '04':
            if opcode == '03':
                if inputs:
                    inp = inputs.pop()
                    a[a[i+1]] = inp
                else:
                    inputs.append(output)
                    return (a,i)
            else:
                v = a[a[i+1]] if o[2] == 0 else a[i+1]
                output = v
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

def find_max_phases_without_feedback(a):
    m = 0
    phases = [0, 1, 2, 3, 4]
    for p in list(itertools.permutations(phases)):
        inputs.append(0)
        for i in range(5):
            inputs.append(p[i])
            run(a[:])
        m=max(m,inputs.pop())
        inputs.clear()
    return m


def run_in_loop(a, phases):
    comps = [(a[:],0), (a[:],0), (a[:],0), (a[:],0), (a[:],0)]
    inputs.append(0)

    for i in range(5):
        inputs.append(phases[i])
        comps[i] = run(comps[i][0])
    
    i = 0
    while True:
        comps[i] = run(comps[i][0], comps[i][1])
        if i == 4 and comps[i][1] == 99:
            return inputs.pop()
        i += 1
        i %= 5


def find_max_phases_with_feedback(a):
    m = 0
    phases = [5,6,7,8,9]
    for p in list(itertools.permutations(phases)):
        o=run_in_loop(a[:],p)
        m=max(o,m)
    inputs.clear()
    return m

a = [int(x) for x in open('d07.txt').read().strip().split(',')]
print(find_max_phases_without_feedback(a[:]))
print(find_max_phases_with_feedback(a[:]))
