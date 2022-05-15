# Graham Scan both working

print("\n\n\n\n")
INF = 99999999999999


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self, i):
        return self.items[i]

    def size(self):
        return len(self.items)


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


def GrahamScanHull(arr):
    P = []
    start = bottomMost(arr)
    output = []
    output.append(start)
    s = Stack()
    n = len(arr)
    for i in range(n-1):
        point = nextPoint(start, arr)
        if point != None:
            P.append(point)
    s.push(P[0])
    s.push(P[1])
    s.push(P[2])
    for i in range(3, n-1):
        if isCounterClockwise(s.peek(1), s.peek(0), P[i]):
            s.push(P[i])
        else:
            s.pop()
            s.push(P[i])
    for i in range(s.size()):
        output.append(s.peek(i))
    return output


# arr = []
# n = int(input("Enter the number of points: "))
# for i in range(n):
#     point = input(f"Enter the point P{i+1}: ").split(" ")
#     arr.append([float(point[0]), float(point[1])])
# print(
#     f"\n____GrahamScan Algorithm____\n\nThe points in the convex hull are {GrahamScanHull(arr)}")

print("\n\n\n\n")

arr = [[3, 1], [5, 5], [0, 0], [1, 4], [9, 6], [7, 0], [5, 2], [3, 3]]
output = []
start = [0, 0]
for i in range(len(arr)):
    output.append(nextPoint(start, arr))
    arr.remove(nextPoint(start, arr))
print(output)
# inf = 99999999999999


# class Stack:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def push(self, item):
#         self.items.insert(0, item)

#     def pop(self):
#         return self.items.pop(0)

#     def peek(self, i):
#         return self.items[i]

#     def size(self):
#         return len(self.items)


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


# def GrahamScan(points):
#     P = []
#     start = leftmost(points)
#     output = []
#     output.append(start)
#     s = Stack()
#     n = len(points)
#     for i in range(n-1):
#         point = Next(start, points)
#         if point != None:
#             P.append(point)
#     s.push(P[0])
#     s.push(P[1])
#     s.push(P[2])
#     for i in range(3, n-1):
#         if isleft(s.peek(1), s.peek(0), P[i]):
#             s.push(P[i])
#         else:
#             s.pop()
#             s.push(P[i])
#     for i in range(s.size()):
#         output.append(s.peek(i))
#     return output


# print("\n________GrahamScan Algorithm________\n\n")
# points = []

# n = int(input("Enter the number of points: "))
# for i in range(n):
#     point = input(f"Enter the point P{i+1}: ").split(" ")
#     points.append([float(point[0]), float(point[1])])
# print(
#     f"\n\nThe required points in the convex hull are: {GrahamScan(points)}\n")

# 8
# 0 0
# 1 1
# 1.5 0.5
# 1.5 -0.5
# 1.2 0.3
# 1.2 -0.3
# 1 0
# 1 -1
