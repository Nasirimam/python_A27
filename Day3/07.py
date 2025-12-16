# write a program to check if the data is even number print cube of it otherwise print square of it

a = int(input("Enter your input: "))

if a % 2 == 0:
    print(a**3)
else:
    print(a**2)
