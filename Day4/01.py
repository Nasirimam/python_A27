# write a program to check if the number is divisible by 3 print fizz if number is divisible
# by 5 print buzz and if both print fizzbuzzerfgg

num = int(input("Enter The num: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
