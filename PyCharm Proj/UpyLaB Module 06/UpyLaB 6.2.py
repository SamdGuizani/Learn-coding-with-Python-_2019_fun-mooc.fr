def top_3_candidats(moyennes):
    l = []
    for i in range(3):
        m = 0
        for c in moyennes:
            if moyennes[c] > m:
                m = moyennes[c]
                meilleur_c = c
        l.append(meilleur_c)
        del moyennes[meilleur_c]
    return tuple(l)


# Code principal
print(top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33}))