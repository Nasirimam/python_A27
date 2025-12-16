# write a program to check or print last value of the list if the value is string and its len should be more then 3
a = eval(input("Enter a list: "))
print(type(a[-1]))
if type(a[-1]) == str and len(a[-1]) > 3:
    print("Okay")
