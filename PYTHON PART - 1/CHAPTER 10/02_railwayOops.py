# import pandas as pd 

# pd.DataFrame()# control and click on the dataFrame()


class RailWay :
    formtype = "Railway Form"

    def printData (self) :
        print("The form name is :",self.formtype)
        print(f"Name is : {self.name}")
        print(self.train)
        print(self.fare)


passenger = RailWay()

passenger.name = "HarryBhai"
passenger.train = "Rajadhani Express"
passenger.fare = 6000

passenger.printData()

