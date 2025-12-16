# write a program to print all the uppercase alphabet present inside a string

a = input("Enter a Sting: ")
out = ""
for i in a:
    
    if "A" <= i <= "Z":
        out += i
print(out)
