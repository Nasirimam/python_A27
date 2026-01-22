class Area:
    def find_area(self, a=None, b=None):
        if a != None and b != None:
            print("Rectangle:", a * b)
        elif a != None:
            print("Square:", a * a)
        else:
            print("No Input Given")


o1 = Area()
o1.find_area()
o1.find_area(5)
o1.find_area(3, 4)
