# Jarvis both working


print("\n\n\n\n")
INF = 99999999999999


def isCounterClockwise(x, y, z):
    if ((y[0] - x[0])*(z[1] - x[1]) - (y[1] - x[1])*(z[0] - x[0])) >= 0:
        return True
    return False


def bottomMost(arr):
    x = INF
    y = INF
    for i in arr:
        if i[0] < x:
            x = i[0]
            y = i[1]
    return [x, y]


def nextPoint(start, arr):
    for i in arr:
        p = 1
        for j in arr:
            if not isCounterClockwise(start, i, j):
                p = 0
                break
        if p and start != i:
            arr.remove(i)
            return i


def JarvisHull(arr):
    start = bottomMost(arr)

    output = []
    output.append(start)
    output.append(nextPoint(start, arr))
    while start != output[-1]:
        output.append(nextPoint(output[-1], arr))
    return output[0:-1]


arr = []
n = int(input("Enter the number of points: "))
for i in range(n):
    point = input(f"Enter point {i+1}: ").split(" ")
    arr.append([float(point[0]), float(point[1])])
print(
    f"\n____Jarvis Algorithm____\n\nThe points in the convex hull are {JarvisHull(arr)}")


print("\n\n\n\n")
# inf = 99999999999999


# def isleft(a, b, c):
#     if ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])) >= 0:
#         return True
#     return False


# def leftmost(points):
#     x = inf
#     y = inf
#     for i in points:
#         if i[0] < x:
#             x = i[0]
#             y = i[1]
#     return [x, y]


# def Next(start, points):
#     for i in points:
#         p = 1
#         for j in points:
#             if not isleft(start, i, j):
#                 p = 0
#                 break
#         if p and start != i:
#             points.remove(i)
#             return i


# def jarvis(points):
#     start = leftmost(points)

#     output = []
#     output.append(start)
#     output.append(Next(start, points))
#     while start != output[-1]:
#         output.append(Next(output[-1], points))
#     return output[0:-1]


# print("\n________Jarvis Algorithm________\n\n")
# points = []
# n = int(input("Enter the number of points: "))
# for i in range(n):
#     point = input(f"Enter the point P{i+1}: ").split(" ")
#     points.append([float(point[0]), float(point[1])])
# print(
#     f"\n\nThe required points in the convex hull are: {jarvis(points)}\n")
