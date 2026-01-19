class online:
    bname = "Nasir"
    badd = "Bihar"

    def __init__(self, cName, cEmail, cAdd, cAcc):
        self.cName = cName
        self.cEmail = cEmail
        self.Add = cAdd
        self.cAcc = cAcc


class offline(online):
    ekyc = True
    adharLink = False


c1 = online("Nasir", "imamnasir73@gmail.com", "mahuwal", 235423454)

print(c1)
