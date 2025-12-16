# write a program  to extracts all the uppercase alphabet ,lowercase alpha ,from a given string
# if number of uppercase are more then lower case then concate upper with lower otherwise print product
# lenth of lowercase with uppercase alpha

a = "abcdEFGH"
lower = ""
upper = ""

for i in a:
    if "A" <= i <= "Z":
        upper += i
    elif "a" <= i <= "z":
        lower += i

if len(upper) > len(lower):
    print(upper + lower)
else:
    print(len(upper) * lower)
