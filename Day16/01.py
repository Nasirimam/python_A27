a = "power star".split()
out = {}

for i in a:
    out[i] = 0
    for j in i:
        if j in "aeiouAEIOU":
            out[i] += 1
print(out)
