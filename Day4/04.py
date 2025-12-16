# write a program to check the number is even or odd but it should divisible by 5 also

num = int(input("Enter The num: "))

if num % 2 == 0:
    if num % 5 == 0:
        print(num, "is even and divisible by 5")
    else:
        print(num, "is even but not divisible by 5")
else:
    print(num, "is odd")
