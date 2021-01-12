inp = open("inputs/d08.txt").read().strip()
w = 25
t = 6

def first():
    layers = list(map("".join, zip(*[iter(inp)] * (w * t))))
    zeros = [x.count("0") for x in layers]
    fewest = layers[zeros.index(min(zeros))]
    print(fewest.count("1") * fewest.count("2"))

def second():
    final = [[0 for x in range(w)] for y in range(t)]
    solved = [[False for x in range(w)] for y in range(t)]
    for l in list(map("".join, zip(*[iter(inp)] * (w * t)))):
        layer = list(map("".join, zip(*[iter(l)] * (w))))
        for i, k in enumerate(layer):
            for j, u in enumerate(layer[i]):
                if not solved[i][j]:
                    if u == "2":
                        continue
                    final[i][j] = u
                    solved[i][j] = True
    
    for line in final:
        print("".join(line).replace("0", " "))

first()
second()
