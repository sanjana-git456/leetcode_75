x = input("Enter: ").replace(" ", "")
def compress(x):
    if len(x) == 1:
        return 1
    s = []
    i = 0
    while i < len(x):
        j = i
        while j < len(x) and x[j] == x[i]:
            j += 1
        s.append(x[i])
        if j-i > 1:
            s.append(j-i)
        i = j
    return ''.join(map(str, s))
print(compress(x))