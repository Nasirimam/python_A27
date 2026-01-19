class Bat:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display(self):
        print(f"Bat Name - {self.name}, Bat Type - {self.type}")


class Ball:
    def __init__(self, bname, btype):
        self.bname = bname
        self.btype = btype

    def display(self):
        print(f"Ball Name - {self.bname}, Ball Type - {self.btype}")


class Cricket(Bat, Ball):
    def __init__(self, name, type, bname, btype, Tname):
        super().__init__(name, type, bname, btype)
        self.Tname = Tname

    def display(self):
        super().display()
        print(f"Team Name - {self.Tname}")


m1 = Cricket("MRF", "Leather", "SG", "Leather", "RCB")
