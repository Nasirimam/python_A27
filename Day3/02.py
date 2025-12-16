# wirte a program to check the character is capital
a = input("Enter first str: ")

if "A" <= a <= "Z":
    print("Upper")


if "a" <= a <= "z":
    print("Lower")


if "0" <= a < "a":
    print("Number")

if a < "0":
    print("spical")

print(ord("0"))
