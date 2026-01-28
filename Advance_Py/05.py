a = ["Hello", 5, 3.5, 10, [1, 2]]

out = []

for i in a:
    if type(i) in [int, bool, complex, float]:
        out += [1]
    else:
        out += [len(i)]
        
print(out)

print([1 if type(i) in [int, bool, complex, float] else len(i) for i in a])
