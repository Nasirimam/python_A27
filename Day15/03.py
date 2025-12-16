a = [1, 2, "3", 5, "Mas"]

for i in a:
    if type(i) != int:
        continue
    print(i, end=" ")
