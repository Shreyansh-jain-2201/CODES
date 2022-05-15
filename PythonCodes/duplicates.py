n = int(input(""))
list1 = input("").split()
list2 = []
output = ""
for i in reversed(list1):
    if i not in list2:
        list2.append(i)
for i in reversed(list2):
    output += i + " "
print(len(list2))
print(output) 