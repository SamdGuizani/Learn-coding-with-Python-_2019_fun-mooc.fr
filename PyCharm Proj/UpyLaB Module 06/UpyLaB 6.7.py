import math


def even(max_nb):
    """Retourne la liste des nombres entiers pairs inférieurs à max_nb"""
    l_even = []
    for i in range(max_nb + 1):
        if i % 2 == 0:
            l_even.append(i)
    return l_even


def prime_numbers(max_nb):
    """Retourne la liste des nombres premiers inférieurs à max_nb"""
    l_prime = []
    for i in range(max_nb + 1):
        if premier(i):
            l_prime.append(i)
    return l_prime


def premier(n):
    """Renvoie vrai si n est un nombre premier"""
    if n == 0 or n == 1:
        res = False
    else:
        k = 2
        res = True
        while k <= int(math.sqrt(n)) and res is True:
            if (n % k) == 0:
                res = False
            k = k + 1
    return res


def prime_odd_numbers(numbers):
    """Reçoit une liste de nombres (numbers) et renvoie un couple d’ensembles contenant respectivement les nombres
    premiers et les nombres impairs présents dans la liste."""
    max_nb = max(numbers)
    l_prime = prime_numbers(max_nb)
    l_even = even(max_nb)

    ens_prime = set()
    ens_odd = set()

    for n in numbers:
        if n not in l_even:
            ens_odd.add(n)

    for n in numbers:
        if n in l_prime:
            ens_prime.add(n)

    return ens_prime, ens_odd


# Code principal
print(prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18]))
