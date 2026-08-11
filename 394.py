x = input("Enter: ")
def decode(x):
    numstack = []
    strstack = []
    currnum = 0
    currstr = ""
    for char in x:
        if char.isdigit():
            currnum = currnum * 10 + int(char)
        elif char == "[":
            numstack.append(currnum)
            strstack.append(currstr)
            currnum = 0
            currstr = ""
        elif char == "]":
            num = numstack.pop()
            prevstr = strstack.pop()
            currstr = prevstr + (currstr*num)
        else:
            currstr += char
    return currstr
print(decode(x))