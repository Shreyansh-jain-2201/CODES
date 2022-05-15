n,m = input("").split()
n,m = int(n), int(m)
marks = []
successful = 0
for i in range(n):
    subjects = list(input(""))
    mark = []
    for j in range(m):
        mark.append(int(subjects[j]))
    marks.append(mark)
print(marks)
