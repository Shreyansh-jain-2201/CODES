n = int(input(""))
x_coord = []
y_coord= []
count_x = 0
count_y = 0
for i in range(n):
    x,y = input("").split()
    x_coord.append(int(x))
    y_coord.append(int(y))

for i in range(n):
    if x_coord.count(x_coord[i]) > count_x:
        count_x = x_coord.count(x_coord[i])
    if y_coord.count(y_coord[i]) > count_y:
        count_y = y_coord.count(y_coord[i])

print(count_y - 1)
print(count_x - 1)
