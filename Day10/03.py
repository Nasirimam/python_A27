a = 6
i = 1
sum = 0
while i < a:
    if a % i == 0:
        sum += i
    i += 1

print(a == sum)
