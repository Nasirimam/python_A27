# ASCII Value
a = "hai hello"
ans = ""
i = 0

while i < len(a):
    if "a" <= a[i] <= "z":
        ans += chr(ord(a[i]) - 32)
    else:
        ans += a[i]
    i += 1
print(ans)
