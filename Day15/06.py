a = [10, "Hello", 3 + 5j, 321]
# op = [1,6]
out = []
for i in a:
    if type(i) == int:
        sum = 0
        for j in str(i):
            sum += int(j)
        out.append(sum)
print(out)