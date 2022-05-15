def returnPos(positions):
    a,b,c = int(positions[0]), int(positions[1]), int(positions[2])
    d = abs(a - b)
    e,f = c-d,c+d
    if a > b:
        a,b = b,a
    if 2*d < a or 2*d < b:
        return -1
        
    if (((a<e and b>e) and (a>c or b<c)) or ((a<c and b>c) and (a>e or b<e))) and e <= 2*d and e>0:
        return e
    elif (((a<f and b>f) and (a>c or b<c)) or ((a<c and b>c) and (a>f or b<f))) and f <= 2*d and f>0:
        return f
    else:
        return -1
    
    
n = int(input(""))
for i in range(0,n):
    print(returnPos(input("").split()))
print(abs(3-1))