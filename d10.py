import math
import queue

# Init stuff
space = [line.strip('\n') for line in open ('d10_test.txt')]
w = len(space[0])
h = len(space)
asteroids = {}

# Give id for each asteroid and initialize table to mark connections
for i in range(h):
    for j in range(w):
        if space[i][j] == '#':
            asteroids[(j,i)] = len(asteroids) + 1
routes = [[0 for x in range(len(asteroids)+1)] for y in range(len(asteroids)+1)]

def find_matches(x,y):
    """ Finds correct matches """
    v = set()
    orig = asteroids[(x,y)]
    for i in range(y,h):
        for j in range(w):
            # Make sure we go through asteroids on this row on only right side
            # Rest of rows are handled from start to end
            if (i == y and j <= x) or (j,i) in v or space[i][j] == '.':
                continue
            # Mark that there's connection
            pname = asteroids[(j,i)]
            routes[orig][pname] = 1
            routes[pname][orig] = 1
            # mark all asteroids reachable the same way as visited for next rounds
            a,b = ((j-x),(i-y))
            g = math.gcd(a,b)
            a /= g
            b /= g
            v = mark_as_visited((j,i),v,a,b)

def mark_as_visited(p,v,xp,yp):
    x = p[0]
    y = p[1]
    if x < 0 or x > w-1 or y < 0 or y > h-1:
        return v
    p = (x + xp, y + yp)
    v.add(p)
    return mark_as_visited(p,v,xp,yp)

def distance(p):
    return round(math.sqrt((point[0] - p[0])**2 + (point[1] - p[1])**2),1)

def solve_200th(p):
    x = p[0]
    y = p[1]
    count = 1
    y_range = (0,y+1)
    x_range = (x,w)
    v = set()
    q = queue.PriorityQueue()
    dists = [[0 for k in range(w)] for l in range(h)]
    angles = [[0 for k in range(w)] for l in range(h)]
    
    for i in range(y_range[0],y_range[1]):
        for j in range(x_range[0],x_range[1]):
            if (j,i) == p or (j,i) in v or space[i][j] == '.':
                continue
            a,b = ((j-x),(i-y))
            g = math.gcd(a,b)
            a /= g
            b /= g
            print(a)
            print(b)
            dists[(y+b)][(x+a)] = distance((a,b))
            v = mark_as_visited((x,y),v,a,b)
    for l in dists:
        print(l)
            #q.put((distance((j,i)), (j,i)))
    #while not q.empty():
        #print("shooted asteroid no. ", count, " at ", q.get()[1])
        #count += 1


# First
for a in asteroids:
    find_matches(a[0],a[1])

for a in asteroids:
    find_matches(x, y):

sums = [sum(l) for l in routes]
name = sums.index(max(sums))
point = [k for (k, v) in asteroids.items() if v == name][0]
print(max(sums), "at", point)

# Second
for l in space:
    print(l)
solve_200th(point)
