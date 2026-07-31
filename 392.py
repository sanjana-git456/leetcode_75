x = input("Enter: ")
y = input("Enter: ")
def substr(x,y):
    l = []
    for i in x:
        if i in y:
            l.append(i)
    f = ''.join(l)
    if y == f:
        return True
    else:
        return False
print(substr(x,y))