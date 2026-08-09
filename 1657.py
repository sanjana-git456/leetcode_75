x = input("Enter: ")
y = input("Enter: ")
def close(x,y):
    cond1 = False
    cond2 = False
    d1 = {}
    d2 = {}
    if set(x) == set(y):
        cond1 = True
    for i in range(len(x)):
        if x[i] in d1:
            d1[x[i]] += 1
        else:
            d1[x[i]] = 1
    for i in range(len(y)):
        if y[i] in d2:
            d2[y[i]] += 1
        else:
            d2[y[i]] = 1
    if sorted(d1.values() == d2.values()):
        cond2 = True
    if cond1 and cond2:
        return True
    else:
        return False
print(close(x,y))