n = int(input(""))
list1 = input("").split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
list1 = list(set(list1))
list1.sort()
print(list1[-1] - list1[0] + 1 - n)