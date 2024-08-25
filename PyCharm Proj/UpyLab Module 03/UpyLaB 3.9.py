initiale = int(input())
cible = int(input())

courante = initiale

while courante != cible:
    print(courante)
    courante = (courante + initiale) % 100
    if courante == cible:
        print('Cible atteinte')
    elif courante == initiale:
        print('Pas trouvé')
        courante = cible