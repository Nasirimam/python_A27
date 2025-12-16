a = "abcstqz"
out = ""

for i in a:
    if i == "z":
        out += "a"
    else:
        out += chr(ord(i) + 1)
print(out)
