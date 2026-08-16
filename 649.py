from collections import deque
x = input("Enter: ")
def dota(x):
    r = deque()
    d = deque()
    n = len(x)
    for i in range(len(x)):
        if x[i] == "R":
            r.append(i)
        else:
            d.append(i)
    while r and d:
        if r[0] < d[0]:
            d.popleft()
            winner = r.popleft()
            r.append(winner+n)
        else:
            r.popleft()
            winner = d.popleft()
            d.append(winner+n)
    if r != []:
        print("Radiant")
    else:
        print("Dire")
dota(x)