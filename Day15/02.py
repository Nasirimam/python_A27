# Extrect the upperalpha using contine

a = "JGHakjdfKJHasfhGfsahf"

for i in a:
    if "a" <= i <= "z":
        continue
    print(i, end=" ")
