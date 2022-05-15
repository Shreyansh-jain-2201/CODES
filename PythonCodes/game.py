def game(n, s):
    print(f"{int(s)} {int(n)}")
    if n == 1:
        return 0
    elif n % 2:
        return game(3*n+1, s+1)
    else:
        return game(n/2, s+1)


s = 0
n = int(input(""))
print(game(n, s))
