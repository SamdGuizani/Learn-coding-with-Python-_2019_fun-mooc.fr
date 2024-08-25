def catalan(n):
    import math
    C = math.factorial(2 * n) / math.factorial(n + 1) / math.factorial(n)
    return C

x = int(input())
print(int(catalan(x)))