n = int(input(""))
for i in range(n):
    x,y,z = input("").split()
    arr = [int(x),int(y),int(z)]
    arr.sort()
    if arr[1] == arr[2]:
        print(f"YES\n{arr[0]} {arr[0]} {arr[1]}")
    else:
        print("NO")