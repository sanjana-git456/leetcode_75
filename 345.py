x = input("Enter: ")
vowels = set('aeiouAEIOU')
def rev(x):
    x = list(x)
    left = 0
    right = len(x) - 1
    while left < right:
        while left < right and x[left] not in vowels:
            left += 1
        while left < right and x[right] not in vowels:
            right -= 1
        x[left], x[right] = x[right], x[left]
        left += 1
        right -= 1
    return ''.join(x)
print(rev(x))