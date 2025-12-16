a = ["Hello", 121, 7777, 12, 3 + 5j, 99]

out = []
i = 0

while i < len(a):
    if type(a[i]) == int:
        if str(a[i]) == str(a[i])[::-1]:
            out.append(a[i])
    i += 1
print(out)
