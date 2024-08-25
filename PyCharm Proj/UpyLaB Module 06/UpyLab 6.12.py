def check_rows(grid):
    """Prend en paramètre une grille sous forme de matrice à deux dimensions (9 x 9) et vérifie si toutes les lignes
    sont valides selon les règles de SUDOKU (c’est-à-dire que sur chaque ligne, chaque chiffre apparaît une et une
    seule fois) """
    test_rows = []  # Liste des tests validité de chaque ligne. Initialisée à liste vide
    for l in grid:
        test_rows.append(check_validity(l))
    verdict = not(False in test_rows)
    return verdict


def check_cols(grid):
    """Prend en paramètre une grille sous forme de matrice à deux dimensions (9 x 9) et vérifie si toutes les
    colonnes sont valides selon les règles de SUDOKU (c’est-à-dire que sur chaque colonne, chaque chiffre apparaît
    une et une seule fois). """
    g = []
    for i in range(len(grid)):
        col = []
        for j in range(len(grid)):
            col.append(grid[j][i])
        g.append(col)

    test_cols = []  # Liste des tests validité de chaque ligne. Initialisée à liste vide
    for l in g:
        test_cols.append(check_validity(l))
    verdict = not (False in test_cols)
    return verdict


def check_regions(grid):
    """Prend en paramètre une grille sous forme de matrice à deux dimensions (9 x 9) et vérifie si toutes les régions
    sont valides selon les règles de SUDOKU (c’est-à-dire que dans chaque région, chaque chiffre apparaît une et une
    seule fois). """
    g = []
    for i in range(0, len(grid), 3):
        region = []
        for j in range(0, len(grid), 3):
            region += grid[j][i:i + 3]
            region += grid[j + 1][i:i + 3]
            region += grid[j + 2][i:i + 3]
            g.append(region)
            region = []

    test_regions = []  # Liste des tests validité de chaque ligne. Initialisée à liste vide
    for l in g:
        test_regions.append(check_validity(l))
    verdict = not (False in test_regions)
    return verdict


def check_validity(l):
    """Vérifie si une liste l de 9 valeurs réponds aux critère de validité SUDOKU"""
    d = {}.fromkeys(range(1, 10), 0)
    for n in l:
        d[n] += 1
    res = True
    for k in d:
        if d[k] != 1:
            res = False
    return res


def check_sudoku(grid):
    """Vérifie si la grille passée en paramètre, sous forme d’une matrice 9 x 9 d’entiers, est une solution au
    problème du SUDOKU. La fonction retournera la réponse (True ou False). """
    if not check_rows(grid):
        res = False
    elif not check_cols(grid):
        res = False
    elif not check_regions(grid):
        res = False
    else:
        res = True
    return res


# code principal
print(check_sudoku([[9, 6, 3, 1, 7, 4, 2, 5, 8],
              [1, 7, 8, 3, 2, 5, 6, 4, 9],
              [2, 5, 4, 6, 8, 9, 7, 3, 1],
              [8, 2, 1, 4, 3, 7, 5, 9, 6],
              [4, 9, 6, 8, 5, 2, 3, 1, 7],
              [7, 3, 5, 9, 6, 1, 8, 2, 4],
              [5, 8, 9, 7, 1, 3, 4, 6, 2],
              [3, 1, 7, 2, 4, 6, 9, 8, 5],
              [6, 4, 2, 5, 9, 8, 1, 7, 3]]))

print(check_sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [2, 3, 4, 5, 6, 7, 8, 9, 1],
              [3, 4, 5, 6, 7, 8, 9, 1, 2],
              [4, 5, 6, 7, 8, 9, 1, 2, 3],
              [5, 6, 7, 8, 9, 1, 2, 3, 4],
              [6, 7, 8, 9, 1, 2, 3, 4, 5],
              [7, 8, 9, 1, 2, 3, 4, 5, 6],
              [8, 9, 1, 2, 3, 4, 5, 6, 7],
              [9, 1, 2, 3, 4, 5, 6, 7, 8]]))
