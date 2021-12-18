class Animal :
    animalType = "mammal"

class Pets(Animal) :
    colour = "white"

class Dog(Pets) :

    @staticmethod
    def bark() :#we can use inside a function too
        print("Bow Bow!!!")

d = Dog()
d.bark()


