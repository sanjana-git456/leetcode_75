x = list(map(int, input("Enter: ").split()))
def zero(x):
    write = 0
    for i in range(len(x)):
        if x[i] != 0:
            x[write] = x[i]
            write += 1
    for i in range(write, len(x)):
        x[i] = 0
    return x
print(zero(x))