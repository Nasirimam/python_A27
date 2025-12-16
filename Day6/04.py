a = "Hello"
b = "bye"
i = 0
st = ""

while i < len(a) or i < len(b):
    if i < len(a):
        st += a[i]
    if i < len(b):
        st += b[i]
    i += 1
print(st)
