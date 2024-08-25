import random

def alea_dice(s):
    random.seed(s)
    d1 = random.randint(1, 6)  # tirage dé 1
    d2 = random.randint(1, 6)  # tirage dé 2
    d3 = random.randint(1, 6)  # tirage dé 3

    dmax = max(d1, d2, d3)  # plus grande valeur
    dmin = min(d1, d2, d3)  # plus petite valeur

    if dmax == 4 and dmin == 1 and (d1 == 2 or d2 == 2 or d3 == 2):
        res = True
    else:
        res = False
    # print((d1, d2, d3))
    # print((p1, p3))
    return res

print(alea_dice(25))