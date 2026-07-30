word1 = input("Enter: ")
word2 = input("Enter: ")
l = []
t = min(len(word1), len(word2))
for i in range(t):
    l.append(word1[i])
    l.append(word2[i])
l.append(word1[t:])
l.append(word2[t:])
print(''.join(l))