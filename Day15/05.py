# WAP to Print Factorial of first 10 natural number and store them in list

out = []

for i in range(1, 11):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    out += [fact]
print(out)
