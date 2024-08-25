def next_line(line):
    if line == []:  # Cas particulier: si ligne est vide
        res = [1]
    else:  # Cas général
        res = []
        k = 0  # Compteur
        n_ref = line[0]  # Initialisation
        '''# La boucle for a pour but de comparer le ième élément de line à une valeur de référence n_ref (initialisée 
        au départ à la 1ere valeur de la liste line). 
        Si la ième valeur lue dans line est égale à la valeur de référence, le compteur k est incrémenté de 1. 
        Cela permet de compter le nombre d'occurrences successives de la valeur de référence. 
        Si la ième valeur lue dans line n'est pas égale à la valeur de référence, cela indique qu'un nouveau nombre est
        détecté. Il devient la valeur de référence et le compteur repart à 1.'''
        for i in range(len(line)):
            if line[i] == n_ref:
                k += 1
            else:
                res.append(k)
                res.append(n_ref)
                n_ref = line[i]
                k = 1
        res.append(k)
        res.append(n_ref)
    return res


# Code principal
print(next_line([1, 2, 1, 1]))
print(next_line([1, 1, 1, 2, 1, 1]))
print(next_line([3, 1, 1, 2, 2, 1]))
print(next_line([1]))
print(next_line([]))
