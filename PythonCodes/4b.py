def numToBinary(length, number):
    # number = str(number)
    output = bin(number).replace("0b", "")
    return "0" * (length - len(output)) + output

# print(type(numToBinary(4, 7)))

def binaryToNum(number):
    number = str(number)
    return int(number,2)
# print(binaryToNum(numToBinary(4, 7)))
def rev(number):
    number = str(number)
    output = number[-1] + number[1:3] + number[0]
    return output
        
print(binaryToNum(rev(numToBinary(4,5)) + rev(numToBinary(4,5))))
# i = 4
# j = 5
# output = binaryToNum(rev(numToBinary(4,i)))) + rev(numToBinary(4,j)))
# print(output)

for i in range(8):
    for j in range(8):
        output = binaryToNum(rev(numToBinary(4,i)) + rev(numToBinary(4,j)))
        print(f"{i}, {j} = {output}")