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


arr = []
for i in range(1, 300):
    if(checkPrime(i)):
        arr.append(i)

print(arr)
print(len(arr))
