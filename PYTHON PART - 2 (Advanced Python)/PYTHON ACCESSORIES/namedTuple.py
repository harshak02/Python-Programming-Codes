from collections import namedtuple

#minisize class we can say 

Car = namedtuple('Car','Milage price colour rate')
xyz = Car(Milage=10, price=100, colour= "Cyan", rate = 1000)
#mini class
print(xyz.colour)

