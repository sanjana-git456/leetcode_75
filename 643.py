x = list(map(int, input("Enter: ").split()))
k = int(input("Enter: "))
def avg(x,k):
    m = 0
    left = 0
    right = k-1
    s = x[left]
    while right <= len(x):
        s = sum(x[left:right])
        a = s // k
        m = max(m, a)
        right += 1
        left += 1
    return m
print(avg(x,k))