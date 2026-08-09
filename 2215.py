x = list(map(int, input("Enter: ").split()))
y = list(map(int, input("Enter: ").split()))
def common(x,y):
    x = set(x)
    y = set(y)
    ans = [list(x-y),list(y-x)]
    return ans
print(common(x,y))