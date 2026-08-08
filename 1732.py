x = list(map(int, input("Enter: ").split()))
def altitude(x):
    s = 0
    ans = 0
    for i in range(len(x)):
        s += x[i]
        ans = max(ans, s)
    return ans
print(altitude(x))