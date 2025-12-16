a = "((()))("

i = 0
arr = []

while i < len(a):
    if a[i] == "(":
        arr.append(a[i])
    elif a[i] == ")":
        arr.pop()
    i += 1
print(len(arr))
