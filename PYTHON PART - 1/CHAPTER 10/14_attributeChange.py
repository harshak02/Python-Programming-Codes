class Base :
    a = None
    
    def getData (self, test) :
        self.a = test
    
    def printData (self) :
        print("The value of a is",self.a)
        
section = Base()
section.getData (4)
section.printData()
