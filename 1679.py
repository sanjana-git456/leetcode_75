x = list(map(int, input("Enter: ").split()))
t = int(input("Enter: "))
def pair(x,t):
    c = 0
    d = {}
    for i in range(len(x)):
        done = False
        a = t - x[i]
        if a in d and d[a] > 0:
            d[a] -= 1
            c += 1
            done = True
        if x[i] not in d and done == False:
            d[x[i]] = 1
        elif done == False:
            d[x[i]] += 1
    return c
print(pair(x,t))