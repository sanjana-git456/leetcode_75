grid = [[3,2,1],[1,7,6],[2,7,7]]
def rc(x):
    r = []
    c = []
    count = 0
    for i in range(3):
        a = []
        r.append(x[i])
        for j in range(3):
            a.append(x[j][i])
        c.append(a)
    for i in range(3):
        for j in range(3):
            if r[i] == c[j]:
                count += 1
    return count
print(rc(grid))