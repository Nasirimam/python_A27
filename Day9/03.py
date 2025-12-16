a = "Hai Hello".split()
dict = {}
i = 0

while i < len(a):
    dict[a[i]] = [a[i], len(a[i]) * 2, a[i][::-1] + str(len(a[i]))]
    i += 1
print(dict)
