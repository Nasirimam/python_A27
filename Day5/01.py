# write a program to reverce a number without using type casting

num = int(input("Enter a number: "))
rev = 0

while num != 0:
    ld = num % 10
    rev = rev * 10 + ld
    num = num // 10
    print("rev: ", rev)
print(rev)
