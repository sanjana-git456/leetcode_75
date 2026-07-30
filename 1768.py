word1 = input("Enter: ")
word2 = input("Enter: ")
l = []
total = min(len(word1), len(word2))
for i in range(total):
    l.append(word1[i])
    l.append(word2[i])
l.append(word1[total:])
l.append(word2[total:])
print(''.join(l))