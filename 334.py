x = list(map(int, input("Enter: ").split()))
def triplet(x):
    first = float('inf')
    second = float('inf')
    for i in x:
        if i <= first:
            first = i
        elif i <= second:
            second = i
        else:
            return True
    return False
print(triplet(x))