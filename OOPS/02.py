class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(self.name, "Average Marks is:", end=" ")
        return sum // len(self.marks)


s1 = Student(
    "Nasir",
    [100, 99, 98, 97],
)
print(s1.avg_marks())
