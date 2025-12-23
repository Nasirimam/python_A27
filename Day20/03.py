def quest():
    a = ["hiee", 10, 3 + 5j, [1, 2], 9.8]
    out = {}

    for i in a:
        if type(i) in [int, complex, float, bool]:
            out[i] = 1
        else:
            out[str(i)] = len(i)
    return out


print(quest())
