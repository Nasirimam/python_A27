a = "Python is very easy".split()
d = {}
i = 0

while i < len(a):
    if i % 2 == 0:
        d[a[i]] = a[i][::-1]
    else:
        d[a[i]] = a[i][::-1] + str(len(a[i] * 2))
    i += 1

print(d)
