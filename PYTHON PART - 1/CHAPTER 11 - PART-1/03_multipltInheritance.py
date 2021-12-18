class Employee :
    company = "Visa"
    eCode = 120#these values will inherit

class FreeLancer :
    company = "Fiverr"
    level = 0

    def upgradeLevel (self) :
        self.level+=1

# class Programmer (Employee,FreeLancer) :
class Programmer (FreeLancer,Employee) :
    name = "Rohith"

pgm = Programmer()
print(pgm.level)
pgm.upgradeLevel
print(pgm.level)
print(pgm.company)#depends upon order of Inheritance



