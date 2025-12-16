# Take four Number find the gratest number

num1 = int(input("Enter The num1: "))
num2 = int(input("Enter The num2: "))
num3 = int(input("Enter The num3: "))
num4 = int(input("Enter The num4: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(num1, "is the greatest number")
elif num2 > num3 and num2 > num4:
    print(num2, "is the greatest number")
elif num3 > num4:
    print(num3, "is the greatest number")
else:
    print(num4, "is the greatest number")
