import math
str1 = input("Enter: ")
str2= input("Enter: ")
def gcdOfStrings(str1, str2):
    if str1+str2 != str2+str1:
        return ""
    g = math.gcd(len(str1), len(str2))
    return str1[:g]
print(gcdOfStrings(str1,str2))