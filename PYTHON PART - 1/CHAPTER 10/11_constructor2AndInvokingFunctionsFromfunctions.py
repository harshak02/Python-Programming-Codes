class Student :
    rollNo = None #these are public acc to C++(my perspection)
    name = None
    points = None

    def __init__(self,x,y) :
        self.name = x
        self.points = y

        print("constructor Invoked")


    @staticmethod 
    def greet() :
        print("Done1!!")#always write this outside only

    def test(self,k) :
        print(f"test {k}")

    def getData(self,z,k) :
        self.rollNo = z
        self.test(k)#invoking a function from other


    def PrintData (self) :
        print(self.rollNo)
        print(self.name)
        print(self.points)


stu1 = Student("harsha",10)
stu2 = Student("manasa",9)

stu1.getData(19,1)
stu2.getData(20,2)
stu1.PrintData()
Student.greet()
stu2.PrintData()
Student.greet()

