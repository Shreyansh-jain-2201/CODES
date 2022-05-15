def checkPrime(num):
    counter = 1
    for i in range(2, num+1):
        if i**2 <= num+1:
            if num % i == 0:
                counter = 0
                break
            else:
                continue
        else:
            break

    if counter == 1:
        return True
    else:
        return False


list1 = []
for i in range(100000):
    print(checkPrime(i))
