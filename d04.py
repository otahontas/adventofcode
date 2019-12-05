start = 236491
stop = 713787
sum1 = 0
sum2 = 0
for x in range(start, stop + 1):
    x = str(x)
    l = len(x)
    if list(x) == sorted(x) and any(x[i] == x[i+1] for i in range(l - 1)):
            sum1 += 1
            if any(x[i] == x[i+1] and
                   (i == 0 or x[i] != x[i-1]) and
                   (i == l - 2 or x[i] != x[i+2]) for i in range(l - 1)):
                sum2 += 1
print(sum1)
print(sum2)
