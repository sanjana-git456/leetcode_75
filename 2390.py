x = input("Enter: ")
def star(x):
    l = []
    for i in range(len(x)):
        if x[i] == '*':
            l.pop()
        else:
            l.append(x[i])
    return ''.join(l)
print(star(x))