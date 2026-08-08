x = list(map(int, input("Enter: ").split()))
def one(x):
    left = 0
    ans = 0
    right = 0
    c = 0
    for right in range(len(x)):
        if x[right] == 0:
            c += 1
        while c > 1:
            if x[left] == 0:
                c -= 1
            left += 1
        ans = max(ans, right-left)
    return ans
print(one(x))