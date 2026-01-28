class A(str):
    def __init__(self, a):
        self.a = a

    def __sub__(self, other):
        out = ""
        for i in self.a:
            if i not in other.a:
                out += i
        return out


ob1 = A("hai")
ob2 = A("hi")
print(ob1 - ob2)
