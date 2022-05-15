# import math


# def solveTheArray(points):
#     def sorting(x):
#         atan = math.atan2(x[1], x[0])
#         if atan >= 0:
#             return (atan, x[1]**2+x[0]**2)
#         else:
#             return (2*math.pi + atan, x[0]**2+x[1]**2)
#     return sorted(points, key=sorting)


# points = [(3, 1), (5, 5), (0, 0), (1, 4), (9, 6), (7, 0), (5, 2), (3, 3)]
# print(f"The sorted array is: {solveTheArray(points)}")


maximum = 1000


def lcs(X, Y, m, n, dp):
    if (m == 0 or n == 0):
        return 0
    if (dp[m - 1][n - 1] != -1):
        return dp[m - 1][n - 1]
    if (X[m - 1] == Y[n - 1]):
        dp[m - 1][n - 1] = 1 + lcs(X, Y, m - 1, n - 1, dp)
        return dp[m - 1][n - 1]
    else:
        dp[m - 1][n - 1] = max(lcs(X, Y, m, n - 1, dp),
                               lcs(X, Y, m - 1, n, dp))
        return dp[m - 1][n - 1]


s1 = "".join(input("S1 : ").split(" "))
s2 = "".join(input("S2 : ").split(" "))
dp = [[-1 for i in range(maximum)] for i in range(len(s1))]
print("Length of LCS : ", lcs(s1, s2, len(s1), len(s2), dp))
