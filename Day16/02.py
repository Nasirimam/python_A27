a = "kabab is love".split()
out = {}

for i in a:
    out[i] = []
    c = 0
    st = ""
    for j in range(len(i)):
        if i[j] in "aerioAEIOU":
            c += 1
        if j % 2 == 0:
            st += i[j]
    out[i] += [i[::-1], c, st]
print(out)
