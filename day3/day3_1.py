fw,sw,x = open('day3_input.txt').read().split('\n')
fw,sw = [x.split(',') for x in [fw,sw]]

def get_points(w):
    x = 0
    y = 0
    points = set()
    dirs = {'D': (0,-1), 'U': (0,1), 'L': (-1,0), 'R': (1,0)}
    for p in w:
        d = p[0]
        l = int(p[1:])
        for _ in range(l):
            x += dirs[d][0]
            y += dirs[d][1]
            points.add((x,y))
    return points

fw_points = get_points(fw)
sw_points = get_points(sw)
common = set()
for pair in fw_points:
    if pair in sw_points:
        common.add((abs(pair[0]),abs(pair[1])))
print(min([sum(x) for x in common]))
