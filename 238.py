x = list(map(int, input("Enter: ").split()))
result = []
for i in range(len(x)):
    fix = x[i]
    p = 1
    for j in range(len(x)):
        if j != i:
            p *= x[j]
    result.append(p)
print(result)

def better(x):
    prefix = [1] * len(x)
    suffix = [1] * len(x)
    result = []
    for i in range(1, len(x)):
        prefix[i] = prefix[i-1] * x[i-1]
    for i in range(len(x)-2, -1, -1):
        suffix[i] = suffix[i+1] * x[i+1]
    for i in range(len(x)):
        result.append(prefix[i] * suffix[i])
    return result
print(better(x))