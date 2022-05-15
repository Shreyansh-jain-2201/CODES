def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = input("").split()
print(factorial(min(int(num[0]), int(num[1]))))
