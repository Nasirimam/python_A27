a = "aaabcbbc"
out = ""
i = 0
count = 1
while i < len(a) - 1:
    if a[i] == a[i + 1]:
        count += 1
    else:
        out += a[i] + str(count)
        count = 1
    i += 1
if a[-1] != a[-2]:
    out += a[-1] + "1"
print(out)