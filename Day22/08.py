class complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def dispaly(self):
        print(self.real, "i +", self.img, "j")

    def add(self, num2):
        realAdd = self.real + num2.real
        imgAdd = self.img + num2.img
        print(realAdd, "i +", imgAdd, "j")


num1 = complex(4, 5)
num1.dispaly()
num2 = complex(2, 1)
num2.add(num1)
