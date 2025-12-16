a = "ava nitin is good aba".split()
out = ""
for i in a:
    if i == i[::-1]:
        out += i + " "
print(out)
