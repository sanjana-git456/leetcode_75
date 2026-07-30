x = list(map(int, input("Enter: ").split()))
y = int(input("Enter: "))
def kids(x,y):
    m = max(x)
    result = []
    for i in range(len(x)):
        if (x[i] + y) >= m:
            result.append(True)
        else:
            result.append(False)
    return result
print(kids(x,y))