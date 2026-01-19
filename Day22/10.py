class Chat:
    obj = {"Nasir": [], "imam": []}

    def toSend(self):
        name = input("Enter A Name: ")
        if name in self.obj:
            msg = input("Enter Your Msg: ")
            self.obj[name] += [msg]
        else:
            print("NA")


class Whatsapp(Chat):
    pass


class Instagram(Chat):
    pass


p1 = Whatsapp()
p1.toSend()
print(p1.obj)
