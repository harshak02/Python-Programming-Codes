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

    def listCreate(self) :
        self.seatList = []
        for i in range (1,self.noOfSeats+1) :
            self.seatList.append(i)

        print(self.seatList)


    def bookTicket(self,seatNo1) :#no need to use self 
        #for seatNo1 coz its totally seperate and we are
        #using this from down main function
        #but we need to create list or anything new here
        #means pls create as a class attribute by
        #writing as xxxx = None

        if(self.noOfSeats>0) :
            print("Your Ticket is confirmed!")
            print("Your seat number is :",seatNo1)
            self.seatList.remove(seatNo1)
            print("The seatList is :")
            print(self.seatList)
            print("Available seats are :",len(self.seatList))
        
        else :
            print("Seats are Not Available!")


    def cancelTicket(self,seatNo2) :
        self.seatList.remove(seatNo2)
        print("Your seat cancellation seat no",seatNo2,"is succesful")
        self.seatList.append(seatNo2)
        print("The available seats now finally are :",len(self.seatList))
        print("The seatList is")
        print(self.seatList)

express = Train("Rajadhani",900,10)
express.printData()
express.listCreate()

seatNo1 = input("Enter the seat to be booked :\n")
seatNo1 = int(seatNo1)

seatNo2 = input("Enter the seat to be cancelled :\n")
seatNo2 = int(seatNo2)


express.bookTicket(seatNo1)
express.cancelTicket(seatNo2)

print("Done!!")



        

        

