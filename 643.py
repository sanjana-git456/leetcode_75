x = list(map(int, input("Enter: ").split()))
k = int(input("Enter: "))
def avg(x,k):
    left = 0
    right = left + k - 1
    s = sum(x[left:right+1])
    m = s/k
    while right <= len(x) - 2:
        s = s - x[left] + x[right + 1]
        a = s / k
        m = max(m, a)
        left += 1
        right += 1
    return m
print(avg(x,k))