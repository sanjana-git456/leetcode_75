x = list(map(int, input("Enter: ").split()))
t = int(input("Enter: "))
def pair(x,t):
    c = 0
    d = {}
    for i in range(len(x)):
        a = t - x[i]
        if a in d:
            d[a] -= 1
            c += 1
        if x[i] not in d:
            d[x[i]] = 1
        else:
            d[x[i]] += 1
    return c
print(pair(x,t))