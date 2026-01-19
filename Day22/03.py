class collage:
    cname = "IQRA Collage"
    cadd = "Bihar"
    _ccode = "123"
    __cpass = "hello123"

    def __init__(self, sName, sEmail, sAdd, sId):
        self.sName = sName
        self.sEmail = sEmail
        self.sAdd = sAdd
        self.sId = sId

    @classmethod
    def dis_cls(cls):
        print(cls.cname, cls.cadd, cls._ccode)

    def dis_obj(self):
        print(self.sName, self.sEmail, self.sAdd, self.sId)


iqra = collage("Nasir", "nasir@gmail.com", "mahuwal", 21)
collage.dis_cls()
iqra.dis_obj()
print(collage._collage__cpass)
collage._collage__cpass = "nasir123"
print(collage._collage__cpass)
