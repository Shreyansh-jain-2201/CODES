n = int(input(""))
teamDeatails = []
for i in range(n):
    teamID = input("")
    facultyID = input("")
    teamDeatails.append([teamID, facultyID])
m = int(input(""))
studentDetails = []
regNos = []
for i in range(m):
    regNo = input("")
    name = input("")
    studentDetails.append([regNo, name])
    regNos.append(regNo)

print(teamDeatails)
print(studentDetails)
teams = []
for i in range(n):
    teams.append(int(m/n))
remaining = m % n
for i in range(remaining):
    teams[i] += 1

students = []
p = 0
for i in range(n):
    students.append(regNos[p:p+teams[i]])
    p += teams[i]


for i in range(n):
    output = {}
    output[teamDeatails[i][1]] = students[i]
    print(output)
