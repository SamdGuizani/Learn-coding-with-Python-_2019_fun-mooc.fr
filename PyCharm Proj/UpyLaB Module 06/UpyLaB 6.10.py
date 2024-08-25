def compteur_lettres(texte):
    """renvoie un dictionnaire contenant toutes les lettres de l’alphabet associées à leur nombre d’apparition dans
    texte. texte ne contient pas de caractères accentués"""
    d = {}.fromkeys('abcdefghijklmnopqrstuvwxyz', 0)
    for c in texte:
        c = c.lower()
        if c in d:
            d[c] = d[c] + 1
    return d


# code principal
print(compteur_lettres('Dessine-moi un mouton.'))