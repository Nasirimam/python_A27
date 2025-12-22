a = "python", "is", "easy", "language"


def capital(a):
    out = ""

    for i in a:
        out += i.capitalize() + " "
    print(out)


capital(a)
