# how to find a char is special or not
char = input("Enter a char: ")

if not ("A" <= char <= "Z" or "a" <= char <= "z" or "0" <= char <= "9"):
    print("special char")
