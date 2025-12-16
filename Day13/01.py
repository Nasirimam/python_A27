# Take string remove duplicate
a = "nasir imam"
out = ""

for i in a:
    if i not in out:
        out += i
print(out)
