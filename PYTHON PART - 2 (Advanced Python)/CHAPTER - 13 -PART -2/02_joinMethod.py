list1 = ["Money","laptop","hardisk","mouse","keyboard",]

sentence = []


sentence.append(" and ".join(list1))
sentence.append(" ~~ ".join(list1))
sentence.append("\n".join(list1))

for item in sentence :
    print(item)

#If index assignment error is there then use append

