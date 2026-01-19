# We have to create a calculater using hybrid model


class addition:
    @staticmethod
    def add(a, b):
        print("sum", a + b)


class subtraction:
    @staticmethod
    def sub(a, b):
        print("sum", a - b)


class new(addition, subtraction):
    @staticmethod
    def mul(a, b):
        print("sum", a * b)


class calculator(new):
    @staticmethod
    def div(a, b):
        print("sum", a / b)


calculator.add(10, 5)
calculator.sub(10, 5)
calculator.mul(10, 5)
calculator.div(10, 5)
