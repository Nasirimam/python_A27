# write a program that to get count of all char
a = "aaabcdcadb"
i = 0
d = {}

while i < len(a):
    d[a[i]] = a.count(a[i])
    i += 1
print(d)
