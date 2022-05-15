import math


def fibonacci(n):
    return int(((1/math.sqrt(5)) * (((1 + math.sqrt(5))/2)**n - ((1 - math.sqrt(5))/2)**n)))


for i in range(1, 10):
    p = fibonacci(i)
    if not p % 2:
        print(p)
