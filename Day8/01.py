# write a program to check string is palindrome or not without using indexing

a = "malayalam"
i = len(a) - 1
out = ""

while i >= 0:
    out += a[i]
    i -= 1

if out == a:
    print("palindrome")
else:
    print("not palindrome")
