for j in range (2,21) :
    f = open(f"MultiplicationTable of {j}.txt","w")
    for k in range(1,21) :
        mul = (j)*(k)
        if(k==20) :
            f.write(f"{j} X {k} = {mul}")

        else :
            f.write(f"{j} X {k} = {mul}\n")

        # break -> this is used to check the pgm running or not
        

    f.close()

print("Done!!")




