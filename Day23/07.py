from abc import ABC, abstractmethod


class clg(ABC):
    @abstractmethod
    def msg():
        pass

    @abstractmethod
    def msg1():
        pass


class demo(clg):
    def msg():
        print("Go to Qspider")

    def msg1():
        print("Go to Deepak Sir....")


ob = demo()
print(demo.msg())
