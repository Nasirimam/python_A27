# write a program to extract all the intiger from a list

a = [12, "hello", 34.5, 67, "world", 89, 23.4, 45]
i = 0
b = []

while i < len(a):
    if type(a[i]) == int:
        b.append(a[i])
    i += 1
print(b)