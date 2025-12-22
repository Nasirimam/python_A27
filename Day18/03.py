str = "10100$100!1011"
str2 = "010101010!^401"


def swap(a):
    out = ""
    for i in a:
        if i == "0":
            out += "1"
        elif i == "1":
            out += "0"
        else:
            out += "#"
    return out


print(swap(str))
print(swap(str2))
