x = list(map(int, input("Enter: ").split()))
def water(x):
    left = 0
    right = len(x) - 1
    area = 0
    while left < right:
        area = max(area, min(x[left], x[right]) * (right-left))
        if (x[left] > x[right]):
            right -= 1
        else:
            left += 1
    return area
print(water(x))