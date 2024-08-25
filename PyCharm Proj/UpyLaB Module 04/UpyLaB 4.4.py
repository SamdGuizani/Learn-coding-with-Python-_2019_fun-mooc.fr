import math


def premier(n):
    """renvoie vrai si n est un nombre premier"""
    if n == 0 or n == 1:
        res = False
    else:
        k = 2
        res = True
        while k <= int(math.sqrt(n)) and res == True:
            if (n % k) == 0:
                res = False
            k = k + 1
    return res


# code principal
x = int(input())
for i in range(0, x):
    if premier(i):
        print(i)
