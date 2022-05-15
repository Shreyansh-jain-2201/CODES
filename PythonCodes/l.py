num = 0
for i in range(21):
    for j in range(21):
        for k in range(21):
            for l in range(21):
                if(i + j + k + l) == 20:
                    num += 1
                    print(i, j, k, l)

print(num)
