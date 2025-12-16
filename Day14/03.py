# Make a casino
import random

win = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


while True:
    you = int(input("Enter You Number: "))
    if win == you:
        print("You Win!🚀")
        break
    elif win > you:
        print(f"Number {win} is winner you pick small Number")
    else:
        print(f"Number {win} is winner you pick large Number")
