class CSsudent:
    stream = "CSE"

    def __init__(self, roll):
        self.roll = roll

    def setAdress(self, address):
        self.address = address

    def getAdress(self):
        return self.address

add = CSsudent(123423462347238688)
add.setAdress("R1C4E the pentigon")
print(add.getAdress())

a = CSsudent(123423462347238688)
b = CSsudent(123423462347238689)
print(a.stream)
print(b.stream)
print(a.roll)

print(CSsudent.stream)
