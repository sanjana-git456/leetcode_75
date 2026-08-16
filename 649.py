from collections import deque
x = input("Enter: ")
def dota(x):
    r = deque()
    d = deque()
    for i in range(len(x)):
        if x[i] == "R":
            r.append(i)
        else:
            d.append(i)
        