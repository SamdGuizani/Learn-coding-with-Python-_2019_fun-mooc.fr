def gagnant(grille):
    # Lister toutes les combinaisons de 4 pions dans la grille
    # lignes horizontales
    combinaisons = []
    for i in range(len(grille)):
        for j in range(len(grille[i]) - 4 + 1):
            grille_ext = grille[i][j:j+4]
            combinaisons.append(grille_ext)
    # lignes verticales
    for i in range(len(grille) - 4 + 1):
        for j in range(len(grille[i])):
            grille_ext = [grille[i][j], grille[i+1][j], grille[i+2][j], grille[i+3][j]]
            combinaisons.append(grille_ext)
    # diagonales gauche-droite
    for i in range(len(grille) - 4 + 1):
        for j in range(len(grille[i]) - 4 + 1):
            grille_ext = [grille[i][j], grille[i + 1][j + 1], grille[i + 2][j + 2], grille[i + 3][j + 3]]
            combinaisons.append(grille_ext)
    # diagonales droite-gauche
    for i in range(len(grille) - 4 + 1):
        for j in range(len(grille[i]) - 4, len(grille[i])):
            grille_ext = [grille[i][j], grille[i + 1][j - 1], grille[i + 2][j - 2], grille[i + 3][j - 3]]
            combinaisons.append(grille_ext)
    # retrait de la liste combinaisons de toutes combinaison contenant une case vide ('V')
    combinaisons = [c for c in combinaisons if 'V' not in c]

    # Teste s'il y a une combinaison gagnante
    res = None
    for c in combinaisons:
        if c == ['R'] * 4:
            res = 'R'
        elif c == ['J'] * 4:
            res = 'J'
    return res


# Code principal
print(gagnant([
    ['R', 'R', 'R', 'J', 'R', 'R', 'J'],
    ['V', 'V', 'R', 'R', 'J', 'R', 'R'],
    ['V', 'V', 'R', 'V', 'R', 'J', 'J'],
    ['V', 'V', 'R', 'V', 'V', 'V', 'R'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
    ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))

print(gagnant([['V', 'V', 'V', 'J', 'R', 'R', 'J'],
               ['V', 'V', 'V', 'R', 'J', 'R', 'R'],
               ['V', 'V', 'V', 'V', 'R', 'J', 'J'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'J'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))

print(gagnant([['V', 'R', 'J', 'J', 'J', 'R', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
               ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
