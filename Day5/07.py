# write a program to seprate all the capital letters from a string

a = "asjdkfrJGHiughdvHGiughZbYGggbsBHdcsiuln"

b = ""
for i in a:
    if i.isupper():
        b += i
print(b)
