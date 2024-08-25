import math

def prime_numbers(nb):
    if type(nb) != int:
        res = None
    elif nb < 0:
        res = None
    else:
        res = []
        i = 0
        while len(res) < nb:
            if premier(i) == True:
                res.append(i)
            i += 1
    return res


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
print(prime_numbers(15))
print(prime_numbers(-2))
print(prime_numbers(3.14))
print(prime_numbers('a'))
