class collage:
    cname = "IQRA Collage"
    cadd = "Bihar"

    def __init__(self, sName, sEmail, sAdd, sId):
        self.sName = sName
        self.sEmail = sEmail
        self.sAdd = sAdd
        self.sId = sId

    @classmethod
    def dis_cls(cls):
        print(cls.cname, cls.cadd)

    def dis_obj(self):
        print(self.sName, self.sEmail, self.sAdd, self.sId)


iqra = collage("Nasir", "nasir@gmail.com", "mahuwal", 21)
collage.dis_cls()
iqra.dis_obj()
