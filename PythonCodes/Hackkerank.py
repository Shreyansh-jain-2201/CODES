# def isGreater(matrix, n, m, i, j):
#     # p = matrix[i][j]
#     # if i + 1 < n:
#     #     if p <= matrix[i+1][j]:
#     #         return False
#     #     elif m > j+1 and (p <= matrix[i+1][j-1] or p <= matrix[i][j-1]):
#     #         return False
#     # if j + 1 < m:
#     #     if n > i+1 and (p <= matrix[i-1][j] or p <= matrix[i-1][j+1]) or p <= matrix[i][j+1]:
#     #         return False
#     # if i + 1 < n and j + 1 < m:
#     #     if n > i+1 and m > j + 1 and (p <= matrix[i-1][j-1] or p <= matrix[i+1][j+1]):
#     #         return False
#     # else:
#     #     return True
#     p = matrix[i][j]
#     if i + 1 < n and j + 1 < m:
#         if i > 0 and j > 0:
#             if p <= matrix[i-1][j-1] or p <= matrix[i-1][j] or p <= matrix[i-1][j+1] or p <= matrix[i][j-1] or p <= matrix[i][j+1] or p <= matrix[i-1][j] or p <= matrix[i-1][j+1] or p <= matrix[i-1][j-1] or p <= matrix[i-1][j] or p <= matrix[i-1][j+1] or p <= matrix[i-1][j-1] or p <= matrix[i-1][j] or p <= matrix[i-1][j+1] or


# # p <= matrix[i+1][j-1] or p <= matrix[i][j-1] p <= matrix[i-1][j-1] or p <= matrix[i-1][j] or p <= matrix[i-1][j+1]:

# n = int(input(""))
# m = int(input(""))
# matrix = []
# for i in range(n):
#     l1 = input().split(" ")
#     for j in range(m):
#         l1[j] = int(l1[j])
#     matrix.append(l1)

# output = 0
# for i in range(n):
#     for j in range(m):
#         if isGreater(matrix, n, m, i, j):
#             output += 1
# print(output)


n = int(input(''))
m = int(input(''))
l = []
c = 0
for i in range(n):
    l.append(input('').split(' '))
for i in range(n):
    for j in range(m):
        l[i][j] = int(l[i][j])
for i in range(n):
    for j in range(m):
        if(i > 0 and j > 0 and i < n-1 and j < n-1):
            if(l[i][j] > l[i+1][j] and l[i][j] > l[i-1][j] and l[i][j] > l[i][j-1] and l[i][j] > l[i][j+1] and l[i][j] > l[i+1][j+1] and l[i][j] > l[i-1][j-1] and l[i][j] > l[i+1][j-1] and l[i][j] > l[i-1][j+1]):
                c = c+1
        elif(i+j == 0 or i+j == n-1 or i+j == 2*(n-1)):
            if(i == 0 and j == 0):
                if(l[i][j] > l[i+1][j] and l[i][j] > l[i+1][j+1] and l[i][j] > l[i][j+1]):
                    c = c+1
            elif(i == n-1 and j == 0):
                if(l[i][j] > l[i-1][j] and l[i][j] > l[i-1][j+1] and l[i][j] > l[i][j+1]):
                    c = c+1
            elif(i == 0 and j == m-1):
                if(l[i][j] > l[i+1][j] and l[i][j] > l[i-1][j-1] and l[i][j] > l[i][j-1]):
                    c = c+1
            else:
                if(l[i][j] > l[i-1][j] and l[i][j] > l[i-1][j-1] and l[i][j] > l[i][j-1]):
                    c = c+1
        else:
            if(i == 0):
                if(l[i][j] > l[i+1][j+1] and l[i][j] > l[i-1][j-1] and l[i][j] > l[i][j+1] and l[i][j] > l[i][j-1] and l[i][j] > l[i+1][j]):
                    c = c+1
            elif(j == 0):
                if(l[i][j] > l[i+1][j+1] and l[i][j] > l[i-1][j] and l[i][j] > l[i][j+1] and l[i][j] > l[i-1][j+1] and l[i][j] > l[i+1][j]):
                    c = c+1
            elif(i == n-1):
                if(l[i][j] > l[i][j+1] and l[i][j] > l[i+1][j+1] and l[i][j] > l[i-1][j] and l[i][j] > l[i-1][j-1] and l[i][j] > l[i][j-1]):
                    c = c+1
            else:
                if(l[i][j] > l[i-1][j] and l[i][j] > l[i-1][j-1] and l[i][j] > l[i][j-1] and l[i][j] > l[i+1][j-1] and l[i][j] > l[i+1][j]):
                    c = c+1
print(c)
