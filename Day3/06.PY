# CHECK THE COLLECTION IS MULTI OR SINGLE DATA TYPE

a = eval(input("Enter your input: "))

datatypes = [list, str, dict, tuple, set]

if type(a) in datatypes:
    print("True")
else:
    print("False")
