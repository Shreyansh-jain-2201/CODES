def numberOFkeys(num):
    return int((int(num[0])-1)*10 + len(num) * (len(num)+1)/2)


n = int(input(""))
for i in range(0, n):
    print(numberOFkeys(input("")))