x = list(map(int, input("Enter: ").split()))
n = int(input("Enter: "))
def flower(x,n):
    count = 0
    if len(x) == 1:
         if x[0] == 0:
              count = 1
         return count >= n
    if x[0] == 0 and x[1] == 0:
            x[0] = 1
            count += 1
    if x[len(x)-1] == 0 and x[len(x)-2] == 0:
        x[len(x)-1] = 1
        count += 1
    for i in range(1,len(x)-1):  
        if x[i] == 0 and x[i+1] == 0 and x[i-1] == 0:
            x[i] = 1
            count += 1
    if count < n:
         return False
    else:
         return True
print(flower(x,n))