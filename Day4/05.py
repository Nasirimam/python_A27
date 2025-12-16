# write a program to check the char is vowel or consonent using nested if

char = input("Enter The Char: ")

if "A" <= char <= "z":
    if char in "aeiouAEIOU":
        print(char, "is a Vowel")
    else:
        print(char, "is a Consonant")
else:
    print("Invalid Input")
