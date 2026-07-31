def compress(chars):
    write = 0
    i = 0
    while i < len(chars):
        j = i
        while j < len(chars) and chars[j] == chars[i]:
            j += 1
        chars[write] = chars[i]
        write += 1
        group_len = j - i
        if group_len > 1:
            for digit in str(group_len):
                chars[write] = digit
                write += 1
        i = j
    return write

x = input("Enter: ").replace(" ", "")
chars = list(x)
length = compress(chars)
print(length)