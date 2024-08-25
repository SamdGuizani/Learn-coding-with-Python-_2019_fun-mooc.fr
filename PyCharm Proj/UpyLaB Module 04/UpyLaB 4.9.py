def bat(joueur1, joueur2):
    if joueur1 == 0:
        if joueur2 == 2:
            res = True
        else:
            res = False
    elif joueur1 == 1:
        if joueur2 == 0:
            res = True
        else:
            res = False
    elif joueur1 == 2:
        if joueur2 == 1:
            res = True
        else:
            res = False
    return res


for i in range(3):
    for j in range(3):
        print(bat(i,j))