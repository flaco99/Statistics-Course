with open("grades.txt") as file:
    data = file.readlines()

grades = data[1:]

tot = 0
topgrade = 0
topstudent = ""
for line in grades:
    name = line.split(" ")[0]
    grade = int(line.split(" ")[1].strip('\n'))
    tot+= grade
    if grade > topgrade:
        topgrade = grade
        topstudent = name
print(topstudent, topgrade)

avg = tot/len(grades)
print(avg)

with open('grades.txt', 'a') as file:
    file.write("\n")
    file.write("avg: " + str(avg) + "\n")
    file.write("top student: "+ topstudent)