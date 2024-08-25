def fibo(n):
    """calcule le n-ième nombre de Fibonacci, avec : n de type int et
    fibo(0) valant 0
    fibo(1) valant 1 et
    fibo(n+1) valant fibo(n-1) + fibo(n)
    si n < 0 : fibo(n) retourne None"""
    f0 = 0
    f1 = 1

    if n < 0:
        print('n doit être positif.')
        return None
    elif n == 0:
        res = f0
    elif n == 1:
        res = f1
    else:
        res = f0 + f1
        f_prec_prec = f0
        f_prec = f1
        for i in range(2,n+1):
            res = f_prec_prec + f_prec
            f_prec_prec = f_prec
            f_prec = res
    return res

x = int(input())
for i in range(0, x):
    print(fibo(i))
