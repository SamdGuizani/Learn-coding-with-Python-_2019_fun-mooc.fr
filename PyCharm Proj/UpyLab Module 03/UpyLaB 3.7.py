import math

a = float(input())
b = float(input())

if a < 0 or b < 0:
    print('Erreur')
else:
    print(math.sqrt(a * b))
