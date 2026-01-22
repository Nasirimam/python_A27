# write a program to make a calculater using magic method
class Cal:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a

    def __mul__(self, other):
        return self.a * other.a

    def __truediv__(self, other):
        return self.a / other.a


c1 = Cal(10)
c2 = Cal(5)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)

print(36 / 4 * (3 + 2) * 4 + 2)
