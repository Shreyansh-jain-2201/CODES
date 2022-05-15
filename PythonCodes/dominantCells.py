n = int(input())
m = int(input())
arr = []
for i in range(n):
    list2 = input().split()
    for j in range(m):
        list2[j] = int(list2[j])
    arr.append(list2)
output = 0
for i in range(n):
    for j in range(m):
        flag = 1
        cell = arr[i][j]
        try:
            if cell <= arr[i][j+1]:
                flag = 0
        except:
            continue
        try:
            if cell <= arr[i][j-1]:
                flag = 0
        except:
            continue
        try:
            if cell <= arr[i+1][j+1]:
                flag = 0
        except:
            continue
        try:
            if cell <= arr[i+1][j]:
                flag = 0
        except:
            continue
        try:
            if cell <= arr[i+1][j-1]:
                flag = 0
        except:
            continue
        try:
            if cell <= arr[i-1][j+1]:
                flag = 0
        except:
            continue
        try:
            if cell <= arr[i-1][j]:
                flag = 0
        except:
            continue
        try:
            if cell <= arr[i-1][j-1]:
                flag = 0
        except:
            continue
    if flag == 1:
        output += 1
print(output)
# 3
# 3
# 1 2 7
# 4 5 6
# 8 8 9
