# write a program to find the greatest number among three number using nested if

a = int(input("Enter The Num in A: "))
b = int(input("Enter The Num in B: "))
c = int(input("Enter The Num in C: "))

if a > b:
    if a > c:
        print(a, "is the greatest number")
    else:
        print(c, "is the greatest number")
else:
    if b > c:
        print(b, "is the greatest number")
    else:
        print(c, "is the greatest number")
