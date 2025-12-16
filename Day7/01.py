a = "ababcdcaba"
# output: 'a4b3c2d1'
res = ""

i = 0

while i < len(a):
    if a[i] not in res:
        res += a[i] + str(a.count(a[i]))
    i += 1
print(res)
