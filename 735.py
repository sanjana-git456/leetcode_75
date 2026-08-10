x = list(map(int, input("Enter: ").split()))
def asteroid(x):
    l = [x[0]]
    for i in range(1,len(x)):
        alive = True
        while l and l[-1] > 0 and x[i] < 0:
            if abs(l[-1]) == abs(x[i]):
                l.pop()
                alive = False
                break
            elif abs(l[-1]) < abs(x[i]):
                l.pop()
            elif abs(l[-1]) > abs(x[i]):
                alive = False
                break
        if alive:
            l.append(x[i])
    return l
print(asteroid(x))