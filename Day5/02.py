# write a program to extreact the all uppercase alphabet from the given string

str = input("Enter a string: ")
out = ""
n = len(str)
i = 0

while i < n:
    if "A" <= str[i] <= "Z":
        out += str[i]
    i += 1
print(out)
