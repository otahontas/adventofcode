import re
import itertools

lines = open("inputs/d14.txt").read().splitlines()

n = 36

def first():
    values = {}
    mask = None
    for line in lines:
        op, arg = line.split(" = ")
        if op == "mask":
            mask = arg
        else:
            mem, val = re.findall(r'(\d+)', line)
            mem = int(mem)

            # Make value "36-bit" string, then combine with mask
            val = bin(int(val))[2:]
            val = ('0' * (n-len(val))) + val
            res = int("".join([x[0] if x[0] != "X" else x[1] for x in tuple(zip(mask, val))]),2)

            values[mem] = res
    print(sum(values.values()))

def second():
    values = {}
    mask = None
    for line in lines:
        op, arg = line.split(" = ")
        if op == "mask":
            mask = arg
        else:
            mem, val = re.findall(r'(\d+)', line)
            val = int(val)

            # Make value "36-bit" string, then combine with mask, but leave X
            mem = bin(int(mem))[2:]
            mem = ('0' * (n-len(mem))) + mem
            masked = "".join([x[0] if x[0] != "0" else x[1] for x in tuple(zip(mask, mem))])

            # Count indexes where X is and apply 0 and 1 to each
            indexes = [ind for ind, char in enumerate(masked) if char == "X"]
            for prods in itertools.product("01", repeat = len(indexes)):
                res = list(masked)
                for i, num in enumerate(prods):
                    res[indexes[i]] = num

                values[int("".join(res), 2)] = val
    print(sum(values.values()))

            
first()
second()
