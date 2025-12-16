# WAP to extract all the uppercase alpha from a string at even index and its ASSCI value should be divisible by 3

a = "PYTHON IS PROGRAMING LANGUAGE"
ans = ""

for i in range(0, len(a), 2):
    if "A" <= a[i] <= "Z" and ord(a[i]) % 3 == 0:
        ans += a[i]
print(ans)
