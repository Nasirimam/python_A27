def remDup(a):
    out = []
    for i in a:
        if i not in out:
            out.append(i)
    return out


def remDupMulti(a):
    out = []
    for i in a:
        if i not in out and a.count(i) > 1:
            out.append(i)
    return out


st = [10, "Hai", 3 + 5j, "Hai", 10, 9.8]
print(remDup(st))
print(remDupMulti(st))
