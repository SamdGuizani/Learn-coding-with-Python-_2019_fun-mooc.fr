def placer_pion(couleur, colonne, grille):
    res = False
    i = 0
    while i < len(grille):
        if grille[i][colonne] == 'V':
            res = True
            grille[i][colonne] = couleur
            i = len(grille) - 1
        i += 1
    return res, grille


# Code principal
print(placer_pion("R", 3, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))

print(placer_pion("J", 4, [['J', 'J', 'J', 'J', 'R', 'R', 'R'],
                     ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
                     ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
                     ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'R', 'V', 'V']]))
