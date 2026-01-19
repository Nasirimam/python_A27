class Student:

    def __init__(self, react, python, sql):
        self.react = react
        self.python = python
        self.sql = sql

    def printMarks(self):
        print("React:", self.react)
        print("Python:", self.python)
        print("SQL:", self.sql)

    def avgMarks(self):
        return (self.react + self.python + self.sql) // 3


s1 = Student(50, 80, 50)
s1.printMarks()
print(s1.avgMarks())
