a = ["Hiee", 10, 3 + 5j, [1, 2], "py"]


def prob1(a):
    out = []
    for i in a:
        if type(i) in [int, complex, bool, float]:
            out.append((i, 1))
        else:
            out.append((i, len(i)))
    print(out)


prob1(a)
