x = list(map(int, input("Enter: ").split()))
def pivot(x):
    leftsum = 0
    total = sum(x)
    for i in range(len(x)):
        if leftsum == total-leftsum-x[i]:
            return i
        leftsum += x[i]
    return -1
print(pivot(x))