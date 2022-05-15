n = int(input(""))
items = {}
for i in range(n):
    s = input().split()
    print(s[0], s[1])
    items[s[0]] = int(s[1])

q = int(input(""))
cart = []
total = 0
for i in range(q):
    s = input().split()
    print(s)
    if(len(s)) == 2:
        cart.append(s[1])
        total += int(items[s[1]])
    elif s[0] == "len":
        print(len(cart))
    elif s[0] == "total":
        print(total)
