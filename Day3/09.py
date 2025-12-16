# write a program to check the char is uppercase,lowercase,num,special

char = input("Enter The char: ")

if "A" <= char <= "Z":
    print("Upper")
elif "a" <= char <= "z":
    print("Lower")
elif "0" <= char <= "9":
    print("Number")
else:
    print("Special")
