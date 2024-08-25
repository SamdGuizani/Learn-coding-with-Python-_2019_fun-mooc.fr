import math

x = float(input())
sinus = x
eps = 1e-6
terme = eps
i = 3
j = 1

# print(sinus, terme, i, j)

while math.fabs(terme) >= eps:
    terme = x**i / math.factorial(i)
    sinus = sinus - j * terme
    i = i + 2
    j = -j
    # print(sinus, terme, i, j)
print(sinus)
