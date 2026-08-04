x = list(map(int, input("Enter: ").split()))
k = int(input("Enter: "))
def consec(x,k):
    left = 0
    c = 0
    m = left + right - 1
    for right in range(len(x)):
        if x[right] == 0:
            c += 1
        while c > k:
            if x[left] == 0:
                c -= 1
            left += 1
        m = max(m, left + right - 1)
    return m