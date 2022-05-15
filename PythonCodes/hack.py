n = int(input(""))
p = int(input(""))
output = 0
arr = []
for i in range(n):
    q = input().split(" ")
    a, b = int(q[0]), int(q[1])
    arr.append([a, b])

for i in range(n):
    for j in range(i+1, n):
        if arr[i][0]/arr[j][0] == arr[i][1]/arr[j][1]:
            output += 1
        print(i, j)
print(output)
