x = list(map(int, input("Enter: ").split()))
y = int(input("Enter: "))
def kids(x,y,m):
    m = max(x)
    for i in range(len(x)):
        if (x[i] + y >= m):
            print("true", end = " ")
        else:
            print("false", end = " ")
kids(x,y,m)