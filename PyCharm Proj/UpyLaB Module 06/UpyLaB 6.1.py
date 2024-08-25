def calcul_prix(produits, catalogue):
    s = 0
    for p in produits:
        s += produits[p] * catalogue[p]
    return s


# Code principal
print(calcul_prix({"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6},
            {"brocoli":1.50, "bouteilles d'eau":1, "bière":2,
             "savon":2.50, "mouchoirs":0.80}))