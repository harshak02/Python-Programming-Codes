favlang = {

}

name1 = input("Enter the name1 :\n")
lang1 = input("Enter the fav lang of student 1 :\n")

name2 = input("Enter the name2 :\n")
lang2 = input("Enter the fav lang of student 2 :\n")

name3 = input("Enter the name3 :\n")
lang3 = input("Enter the fav lang of student 3 :\n")

name4 = input("Enter the name4 :\n")
lang4 = input("Enter the fav lang of student 4 :\n")

updateddict = {
    name1 : lang1,
    name2 : lang2,
    name3 : lang3,
    name4 : lang4
}

favlang.update(updateddict)

# favlang.items()
print(favlang)

k = favlang.items()
print(k)# coz we are just printing this in a
#different manner so it works out

# favlang[name1] = lang1
# favlang[name2] = lang2
# favlang[name3] = lang3
# favlang[name4] = lang4

# print(favlang)

