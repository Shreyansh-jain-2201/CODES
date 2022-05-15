def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def gcd2(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd1(a, b):
    if b == 0:
        return a
    else:
        return gcd1(b, a % b)


print(gcd(65765200, 654620))
print(gcd1(657652, 65462))
print(gcd2(657652, 65462))
