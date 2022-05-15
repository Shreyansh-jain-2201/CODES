def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def hcf(arr):
    if len(arr) == 2:
        return gcd(arr[0], arr[1])
    else:
        a = gcd(arr[0], arr[1])
        arr = [a] + arr[2:]
        return hcf(arr)


print(hcf([2, 4, 8]))
