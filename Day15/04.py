a = "How are you all".split()
# op = [1, 2, 2, 1]
out = []
for i in a:
    count = 0
    for j in i:
        if j in "aeiouAEIOU":
            count += 1
    out += [count]
print(out)
