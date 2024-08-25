def intersection(v, w):
    res = ''

    # Créer une liste de toutes les sous chaines possibles de v dans un ordre de taille décroissante.
    v_sous_chaines = []
    for k in range(len(v), 0, -1):
        for i in range(len(v)):
            if i + k <= len(v):
                v_sous_chaines.append(v[i:i + k])

    # Tester la présence de chaque sous chaine de v dans w.
    # La liste Results stock la valeur True ou False de chaque test.
    results = []
    for i in range(len(v_sous_chaines)):
        results.append(v_sous_chaines[i] in w)

    # Recherche de la première (éventuelle) occurrence de sous chaines de v dans w
    i = 0
    while i < len(results):
        if results[i] == True:
            res = v_sous_chaines[i]
            i = len(results) - 1
        i += 1

    return res


# Code principal
print(intersection('programme', 'grammaire'))
