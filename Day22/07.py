class Train:
    RName = "Indian Railways"

    def __init__(self, tname, tnum, type):
        self.tname = tname
        self.tnum = tnum
        self.type = type

    def display(self):
        print(
            "Train Details:",
            f"Name:{self.tname}, Number:{self.tnum}, Type:{self.type}",
            end="",
        )


class Passenger(Train):
    def __init__(self, tname, tnum, type, pname, page):
        super().__init__(tname, tnum, type)
        self.pname = pname
        self.page = page

    def display(self):
        super().display()
        print(
            f", Passenger Name:{self.pname}, Age:{self.page}",
            end="",
        )


class Confirm(Passenger):
    def __init__(self, tname, tnum, type, pname, page, pnr, seat):
        super().__init__(tname, tnum, type, pname, page)
        self.pnr = pnr
        self.seat = seat

    def display(self):
        super().display()
        print(f", PNR:{self.pnr}, Seat No:{self.seat}")


p1 = Confirm("Rajdhani", 12345, "Express", "Amit", 30, "PNR123456", "B1-45")
p1.display()
p2 = Confirm("Bihar Sampark", 12345, "SF", "Nasir", 23, "PNR123456", "B2-20")
p2.display()
