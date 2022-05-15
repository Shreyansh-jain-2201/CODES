def fibonacci(n):
    output = [1, 1]
    for i in range(n + 5):
        output.append(output[-1] + output[-2])
    return output
    

n = int(input(""))
output = ""
f = fibonacci(n)
for i in range(1, n+1):
    if i in f:
        output += "O"
    else:
        output += "o"

        
print(fibonacci(n))
print(output)