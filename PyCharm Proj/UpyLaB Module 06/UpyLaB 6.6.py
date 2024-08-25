def valeurs(dico):
    """Retourne la liste de valuer d'un dictionnaire, triée selon les clés"""
    l_keys = list(dico.keys())
    l_keys.sort()
    res = []
    for k in l_keys:
        res.append(dico[k])
    return res


# Code principal
print(valeurs({'three': 'trois', 'two': 'deux', 'one': 'un'}))