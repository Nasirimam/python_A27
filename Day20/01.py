def up():
    a = "PyThOn"
    out = ""
    for i in a:
        if "A" <= i <= "Z":
            out += i
    return out


print(up())
