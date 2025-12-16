a = ["Hello", 3.5, 3, [1, 2], 3 + 5j]
out = []
for i in a:
    if type(i) in [int, bool, complex, float]:
        out += [1]
    else:
        out += [len(i)]
print(out)
