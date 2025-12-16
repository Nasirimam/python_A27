a = [1, 2, 3.5, 4, 5]

for i in a:
    if type(a[0]) != type(i):
        print("Hetro")
        break
else:
    print("Homo")
