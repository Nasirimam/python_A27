class offline:
    bank_name = "SBI"
    bank_add = "Delhi"
    bank_IFSC = "SBIN0000456"

    def __init__(self, cName, cEmail, cAdd, cId, cBal=0):
        self.cName = cName
        self.cEmail = cEmail
        self.cAdd = cAdd
        self.cId = cId
        self.cBal = cBal

    def disp_obj(self):
        print(self.cName, self.cEmail, self.cAdd, self.cId, self.cBal)

    def credit(self, amount):
        self.cBal += amount
        print(f"{amount} Credit Cash and total bal {self.cBal}")

    def debit(self, amount):
        if self.cBal < amount:
            print("Isufficient Ammont In you Acc")
        else:
            self.cBal -= amount
            print(f"{amount} deducted from you acc and total left={self.cBal}")

    def showBal(self):
        print(self.cBal)


class online(offline):
    def __init__(self, cName, cEmail, cAdd, cId, cBal, caddhar, PAN):
        super().__init__(cName, cEmail, cAdd, cId, cBal)
        self.caddhar = caddhar
        self.PAN = PAN

    def kyc(self):
        if self.caddhar != None and self.PAN != None:
            print("KYC Pending")
        else:
            print("KYC Done")

    def credit(self, amount):
        return super().credit(amount)

    def debit(self, amount):
        return super().debit(amount)

    def disp_obj(self):
        super().disp_obj()
        print(self.caddhar, self.PAN)


c1 = online("nasir", "jhasdf", "asd", 123, 345, 3453453, 453453)
c1.disp_obj()
