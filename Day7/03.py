a = "How are you all"
ans = ""
i = 0

while i < len(a):
    if a[i] == " ":
        ans += "_"
    else:
        ans += a[i]
    i += 1
print(ans)
