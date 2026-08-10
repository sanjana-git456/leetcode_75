x = list(map(int, input("Enter: ").split()))
def asteroid(x):
    l = [x[0]]
    for i in range(1,len(x)):
        if l[-1] > 0 and x[i] < 0:
            l.append(max(abs(x[i]),abs(l[-1])))
        elif l[-1] > 0 and x[i] < 0 and abs(l[-1]) == abs(x[i]):
            l.pop()