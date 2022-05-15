n = int(input(""))
ranks = input("").split()
a,b = input("").split()
output = 0
for i in range(int(a),int(b),1):
    output += int(ranks[i-1])
print(output)