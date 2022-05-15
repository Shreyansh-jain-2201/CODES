def gcd(a,b):
    if b == 0:
        return a
    else:
        print(a,b)
        return gcd(b,a%b)


print(gcd(1098765,124556550))