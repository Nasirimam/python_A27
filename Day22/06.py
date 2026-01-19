class Ten:

    def __init__(self, school, obtainMarks10):
        self.school = school
        self.obtainMarks10 = obtainMarks10

    def display(self):
        print("School:", self.school, end="/")
        print("School Marks:", self.obtainMarks10)


class Twelve(Ten):
    def __init__(self, school, obtainMarks10, collage, obtainMarks12):
        super().__init__(school, obtainMarks10)
        self.collage = collage
        self.obtainMarks12 = obtainMarks12

    def display(self):
        super().display()
        print("Collage Name:", self.collage, end="/")
        print("12 Marks:", self.obtainMarks12)


class Grad(Twelve):
    def __init__(self, school, obtainMarks10, collage, obtainMarks12, gcollage, gmarks):
        super().__init__(school, obtainMarks10, collage, obtainMarks12)
        self.gcollage = gcollage
        self.gmarks = gmarks

    def display(self):
        super().display()
        print("Collage Name:", self.gcollage, end="/")
        print("Graducation Marks:", self.gmarks)


s1 = Grad("IQRO", 480, "ZA Collage", 300, "MMHU", 318)
s1.display()
