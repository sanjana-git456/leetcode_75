grid = [[3,2,1],[1,7,6],[2,7,7]]
def rc(x):
    r = []
    c = []
    for i in range(3):
        r.append(x[i])
    return r
print(rc(grid))