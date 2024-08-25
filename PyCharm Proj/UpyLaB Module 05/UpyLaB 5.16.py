# Definition fonctions
def distance_mots(mot_1, mot_2):
    dist_hamming = 0
    for i in range(len(mot_1)):
        if mot_1[i] != mot_2[i]:
            dist_hamming += 1
    return dist_hamming


def correcteur(mot, liste_mots):
    # Extraction des mots de même longueur que variable mot à partir de liste_mots
    liste_mots_candidats = []
    for i in range(len(liste_mots)):
        if len(mot) == len(liste_mots[i]):
            liste_mots_candidats.append(liste_mots[i])
    # Calcul distances de variable mot aux mots de liste liste_mots_candidats
    liste_distances = []
    for i in range(len(liste_mots_candidats)):
        liste_distances.append(distance_mots(mot, liste_mots_candidats[i]))
    # Sélection du mot correct
    distance_min = min(liste_distances)
    index_mot_correct = liste_distances.index(distance_min)
    mot_correct = liste_mots_candidats[index_mot_correct]
    return mot_correct


# Code principal
print(correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"]))
