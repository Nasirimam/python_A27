a = ["hai", 10, "hai", 3.5, 10, 3 + 5j, "hai"]
i = 0
out = []

while i < len(a):
    if a[i] not in out and a.count(a[i]) > 1:
        out.append(a[i])
    i += 1
print(out)
