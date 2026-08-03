x = input("Enter: ")
k = int(input("Enter: "))
def vowel(x,k):
    left = 0
    right = left+k-1
    s = x[left:right+1]
    v = ['a', 'e', 'i', 'o', 'u']
    c = 0
    for i in s:
        if i in v:
            c += 1
    m = c
    while right <= len(x) - 2:
        if x[left] in v:
            c -= 1
        if x[right+1] in v:
            c += 1
        m = max(m,c)
        left += 1
        right += 1
    return m