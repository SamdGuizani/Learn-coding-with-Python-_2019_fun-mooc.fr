def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    argent_recu = x20 * 20 + x10 * 10 + x5 * 5 + x2 * 2 + x1 * 1
    # print(prix)
    # print(argent_recu)
    if prix > argent_recu:
        res20 = None
        res10 = None
        res5 = None
        res2 = None
        res1 = None
    else:
        rendu = argent_recu - prix

        res20 = rendu // 20
        rendu = rendu - res20 * 20

        res10 = rendu // 10
        rendu = rendu - res10 * 10

        res5 = rendu // 5
        rendu = rendu - res5 * 5

        res2 = rendu // 2
        rendu = rendu - res2 * 2

        res1 = rendu
    return res20, res10, res5, res2, res1


print(rendre_monnaie(56, 5, 0, 0, 0, 0))
