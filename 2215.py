x = list(map(int, input("Enter: ").split()))
y = list(map(int, input("Enter: ").split()))
def common(x,y):
    x = set(x)
    y = set(y)
    ans = []
    a = []
    b = []
    for i in x:
        if i not in y:
            a.append(i)
    ans.append(a)
    for j in y:
        if j not in x:
            b.append(j)
    ans.append(b)
    return ans
print(common(x,y))