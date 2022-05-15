n = int(input(""))
for i in range(n):
    a = input("")
    b = a[0]
    c = a[-1]
    a = a[1:-1]
    for i in range(0,len(a),2):
        b += a[i]
    b = b + c
    print(b)