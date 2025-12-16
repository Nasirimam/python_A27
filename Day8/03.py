a = ["python", 35, "ab", 3 + 5j, [1, 2, 3], "star", "Django"]

dict = {}
i = 0

while i < len(a):
    if type(a[i]) == str:
        if i % 2 == 0:
            dict[a[i]] = a[i][::-1] + str(len(a[i]) * 2)
        else:
            dict[a[i]] = len(a[i]) * 2
    i += 1
print(dict)
