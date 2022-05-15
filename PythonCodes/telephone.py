def makeTelephone(number):
    if len(number) < 11:
        return False
    
    while(len(number) > 11):
        if number[0] != "8":
            number = number[1:]
        if number[0] == "8":
            break
    
    if len(number)> 11:
        number = number[0:11]
    if number[0] == "8" and len(number) == 11:
        return True
    else:
        return False
    
n = int(input(""))
for i in range(n):
    m = int(input(""))
    number = input("")
    if makeTelephone(number):
        print("YES")
    else:
        print("NO")