class Base :
    a = 0
    
    def getData (self, test) :
        self.a = test
    
    def printData (self) :
        print("The value of a is",self.a)
        
        
    @staticmethod
    def greet() :
        print ("Good morning Sir!!")
        
section = Base()
#section.a = 4
section.getData(4)
section.printData()
Base.greet()

print("Done!!")
