class Number :
    num = None

    def __init__(self,num) :
        self.num = num

    def __add__(self,n2) :
        print("The addition is in process")
        result = self.num + n2.num
        return result#this is crct

    def __mul__(self,n2) :
        print("Lets Multiply!")
        result1 = self.num * n2.num
        return result1

    def __str__(self) :
        print("str is working!")
        return f"The number is {self.num}"#compulsorily write like this

    def __len__(self) :
        print("Len is used")
        return 1


n1 = Number(4)
n2 = Number(5)
print(n1)
print(n2)

num1 = len(n1)
print(num1)

print(len(n2))



