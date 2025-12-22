# capatialize() : it is a function which is use to capitailze the first
# Letter

a = "pyThOn"


def cap(str):
    newstr = ""
    for i in range(len(str)):
        if i == 0 and "a" <= a[i] <= "z":
            newstr += chr(ord(str[i]) - 32)
        elif "A" <= a[i] <= "Z" and i != 0:
            newstr += chr(ord(str[i]) + 32)
        else:
            newstr += str[i]
    return newstr


print(cap(a))
