import math
x = input("Enter: ")
y = input("Enter: ")
def gcdOfStrings(str1, str2):
    if x+y != y+x:
        return ""
    g = math.gcd(len(str1), len(str2))
    return str1[:g]
print(gcdOfStrings(x,y))