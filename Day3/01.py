# write a program to find palinderome
a = str(input("Enter first str: "))
b = str(input("Enter sec str: "))


if a == b[::-1]:
    print("Yes")
else:
    print("No")
