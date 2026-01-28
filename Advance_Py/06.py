a = [2, 8.5, "Hello", 8, 7, [1, 2]]

# print([i * i if type(i) == int and i % 2 == 0 else i for i in a])

b = [1, 2, 3, 4, 5, 6, 8, 9, 0]

print({i * i if i % 2 == 0 else i**3 for i in b})
