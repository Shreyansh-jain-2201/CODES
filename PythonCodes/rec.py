# def isRectangle(x, y, z, w):
#     if x[0] == z[0] and x[1] == y[1] and y[0] == w[0] and z[1] == w[1]:
#         return True
#     return False


# def area(x, y, z, w):
#     return abs(x[0] - y[0]) * abs(x[1] - z[1])


# n = int(input(""))
# coordinates = []
# x_coordinates = []
# y_coordinates = []
# for i in range(n):
#     x, y = input().split()
#     x_coordinates.append(int(x))
#     y_coordinates.append(int(y))
#     coordinates.append([int(x), int(y)])

# maximum = 0

# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             for l in range(n):
#                 if i != j and i != k and i != l and j != k and j != l and k != l:
#                     if isRectangle(coordinates[i], coordinates[j], coordinates[k], coordinates[l]) and area(coordinates[i], coordinates[j], coordinates[k], coordinates[l]) > maximum:
#                         maximum = area(
#                             coordinates[i], coordinates[j], coordinates[k], coordinates[l])

# print(maximum)
# print(coordinates)
# 8
# -5 8
# 4 8
# -4 4
# 5 4
# -5 -3
# 4 -3
# -4 -1
# 5 -1

c = [[-5, 8], [4, 8], [-4, 4], [5, 4], [-5, -3], [4, -3], [-4, -1], [5, -1]]
c.sort()
print(c)


def isRectangle(y, w, x, z):
    if x[0] == z[0] and x[1] == y[1] and y[0] == w[0] and z[1] == w[1]:
        return True
    return False


def area(y, w, x, z):
    return abs(x[0] - y[0]) * abs(x[1] - z[1])


n = int(input(""))
coordinates = []
for i in range(n):
    x, y = input().split()
    coordinates.append([int(x), int(y)])
coordinates.sort()
maximum = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    if isRectangle(coordinates[i], coordinates[j], coordinates[k], coordinates[l]) and area(coordinates[i], coordinates[j], coordinates[k], coordinates[l]) > maximum:
                        maximum = area(
                            coordinates[i], coordinates[j], coordinates[k], coordinates[l])
print(maximum)
