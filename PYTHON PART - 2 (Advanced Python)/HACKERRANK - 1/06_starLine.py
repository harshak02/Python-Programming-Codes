if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        # *means it is used for more than one objects
        name, *line = input().split()#prints and gives first word to name
        scores = list(map(float, line))#this line becomes list
        student_marks[name] = scores
    query_name = input()

    list1 = student_marks.keys()

    for item in list1 :
        if(item == query_name) :
            temp = sum(student_marks[item])
            avg = temp/3
            break

    string = "{:.2f}".format(avg)

    print(string)


'''
The * is being used to grab additional returns from the split statement. So if you had: >>> first, *rest = input().split() >>> print(first) >>> print(*rest) and ran it and typed in "hello my name is bob" It would print out hello ['my', 'name', 'is', 'bob']'''

