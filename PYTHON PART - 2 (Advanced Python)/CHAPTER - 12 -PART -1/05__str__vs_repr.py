class Base :
    val = None

    def __init__(self,num) :
        self.val = num

    def __str__(self) :
        return  f"The value of attribute is {self.val}"

    def __repr__(self) :
        return f"Im repr method"

b = Base(4)
print(b)
print(repr(b))

