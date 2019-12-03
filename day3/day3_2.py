fw,sw,x = open('day3_input.txt').read().split('\n')
fw,sw = [x.split(',') for x in [fw,sw]]

def get_points(w):
    x = 0
    y = 0
    steps = 0
    points = {}
    dirs = {'D': (0,-1), 'U': (0,1), 'L': (-1,0), 'R': (1,0)}
    for p in w:
        d = p[0]
        l = int(p[1:])
        for _ in range(l):
            x += dirs[d][0]
            y += dirs[d][1]
            steps += 1
            if (x,y) not in points:
                points[(x,y)] = steps
            else:
                points[(x,y)] += steps
    return points

fw_points = get_points(fw)
sw_points = get_points(sw)
steps = []
for pair in fw_points:
    if pair in sw_points:
        steps.append(fw_points[pair]+sw_points[pair])
print(min(steps))
