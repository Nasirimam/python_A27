a = "aaabcbbc"
i = 0
c = 1
ans = ""

while i < len(a) - 1:
    if a[i] == a[i + 1]:
        c += 1
    else:
        ans += a[i] + str(c)
        c = 1
    i += 1
ans += a[-1] + str(c)
print(ans)
