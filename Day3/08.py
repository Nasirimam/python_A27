# if the number is single digit or 2 digit or four digit number

num = int(input("Enter The Number: "))

if 0 <= num <= 9:
    print("1-Digit")
elif 10 <= num <= 99:
    print("2-Digit")
elif 100 <= num <= 999:
    print("3-Digit")
elif 1000 <= num <= 9999:
    print("4-Digit")
