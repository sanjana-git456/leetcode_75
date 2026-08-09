x = list(map(int, input("Enter: ").split()))
def unique(x):
    d = {}
    l = []
    for i in range(len(x)):
        if x[i] not in d:
            d[x[i]] = 1
        else:
            d[x[i]] += 1
    for i in d:
        if d[i] in l:
            return False
        l.append(d[i])
    return True
print(unique(x))