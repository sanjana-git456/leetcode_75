x = input("Enter: ")
y = input("Enter: ")
def substr(x,y):
    i = 0
    j = 0
    while j < len(x):
        if i < len(y) and x[i] == x[j]:
            i += 1
        j += 1
    return i == len(y)
print(substr(x,y))