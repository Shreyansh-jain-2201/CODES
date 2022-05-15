x = input().split(" ")
x = float(x)
y = float(y)
if x < y and not x % 5:
    y -= (x + 0.5)
print("{:.2f}".format(y))
