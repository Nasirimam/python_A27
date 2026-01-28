li = [101, 22, 43, 465, "asd", "asd"]

print([i for i in li if type(i) == int and str(i) == str(i)[::-1]])
