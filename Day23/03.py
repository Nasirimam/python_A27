# Method overiding
class A:
    def show_Data(self):
        print("Hello World")


class B(A):
    def show_Data(self):
        print("Hello Earth")


o1 = B()
o1.show_Data()
