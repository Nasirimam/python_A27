# Making of basic fist calculater

num1 = float(input("Enter first number: "))
oprater = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if oprater == "+":
    print(num1 + num2)
elif oprater == "-":
    print(num1 - num2)
elif oprater == "*":
    print(num1 * num2)
elif oprater == "/":
    if num2 == 0:
        print("Error! Divison by zero.")
    else:
        print(num1 / num2)
else:
    print("Invalid operator")
