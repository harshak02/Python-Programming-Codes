list1 = ["harsha","harrybhai","divya","sruthi"]

name = input("Enter the name :\n")

num = list1.count(name)

if(num == 0) :
    print("The name is not present in the list :-(")

else :
    print("The name is present in the list and count is :",num)


if (name in list1) :
    print("The name is present in the list :-)")

else :
    print("The name is not present in the list :-(")


    