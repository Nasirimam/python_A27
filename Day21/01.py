a = "python is programing language"
b = "hello my name is nasir imam"


def makeDict(a):
    a = a.split()
    out = {}
    for i in a:
        if i[0] not in out:
            out[i[0]] = []
        out[i[0]].append(i)
    return out


print(makeDict(a))
print(makeDict(b))
