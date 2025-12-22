# Write a program to find the sum of number in email id
a = "imamnasir73@gmail.com"


def sumEmail(email):
    sum = 0
    for i in email:
        if "0" <= i <= "9":
            sum += int(i)
    return sum


print(sumEmail(a))
