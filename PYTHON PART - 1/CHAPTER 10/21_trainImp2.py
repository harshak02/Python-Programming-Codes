class Train :
    name = None
    fare = None
    noOfSeats = None
    seatList = None#create here only anything variable

    def __init__(self,name1,fare1,noOfSeats1) :
        self.name = name1
        self.fare = fare1
        self.noOfSeats = noOfSeats1

        print("Constructor Invoked!")

    def printData(self) :
        print("The name of Train is :",self.name)
        print("The fare of the Ticket is",self.fare)
        print("The num. of seats available is ",self.noOfSeats)


    def bookTicket(self,seatNo1,seatList) :#here no need to
        #use self here coz we sent list from the main function


        if(self.noOfSeats>0) :
            print("Your Ticket is confirmed!")
            print("Your seat number is :",seatNo1)
            seatList.remove(seatNo1)
            print("The seatList is :")
            print(seatList)
            print("Available seats are :",len(seatList))
        
        else :
            print("Seats are Not Available!")


    def cancelTicket(self,seatNo2,seatList) :
        seatList.remove(seatNo2)
        print("Your seat cancellation seat no",seatNo2,"is succesful")
        seatList.append(seatNo2)
        print("The available seats now finally are :",len(seatList))
        print("The seatList is")
        print(seatList)

express = Train("Rajadhani",900,10)
express.printData()
SeatList = []
for i in range (1,express.noOfSeats+1) :#here we need to use the express. but 
    #not self. in the main function
    SeatList.append(i)
print(SeatList)

seatNo1 = input("Enter the seat to be booked :\n")
seatNo1 = int(seatNo1)

seatNo2 = input("Enter the seat to be cancelled :\n")
seatNo2 = int(seatNo2)


express.bookTicket(seatNo1,SeatList)
express.cancelTicket(seatNo2,SeatList)

print("Done!!")
