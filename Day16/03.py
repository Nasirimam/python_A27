a = int(input("Enter A Num: "))

fl = 0
mid = 0

temp = str(a)

for i in range(len(temp)):
    if i == 0 or i == len(temp) - 1:
        fl += int(temp[i])
    else:
        mid += int(temp[i])

if fl == mid:
    print("Xylom")
else:
    print("Pyloyem")
