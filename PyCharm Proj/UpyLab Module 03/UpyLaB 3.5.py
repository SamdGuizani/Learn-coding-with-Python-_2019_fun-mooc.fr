x = int(input())
y = int(input())

"""Détermine si x est diviseur de y ou si y est diviseur de x"""

if x % y != 0 and y % x !=0:
    print(True)
else:
    print(False)
