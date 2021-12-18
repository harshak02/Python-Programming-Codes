class Sample :
    name = None

    def __init__(self,name1) :
        self.name = name1

    def __init__(slf,name1) :# we can se any set of parameters
        slf.name = name1#overwrites this

obj = Sample("Harry")
print(obj.name)
# down do works with obj name and in class do works with self name
