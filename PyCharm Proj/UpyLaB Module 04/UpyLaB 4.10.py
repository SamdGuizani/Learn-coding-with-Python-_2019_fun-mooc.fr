import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2


def bat(joueur1, joueur2):
    if joueur1 == PIERRE:
        if joueur2 == PIERRE:
            res = 0
        elif joueur2 == FEUILLE:
            res = 1
        elif joueur2 == CISEAUX:
            res = -1
    elif joueur1 == FEUILLE:
        if joueur2 == PIERRE:
            res = -1
        elif joueur2 == FEUILLE:
            res = 0
        elif joueur2 == CISEAUX:
            res = 1
    elif joueur1 == CISEAUX:
        if joueur2 == PIERRE:
            res = 1
        elif joueur2 == FEUILLE:
            res = -1
        elif joueur2 == CISEAUX:
            res = 1
    return res


def manche(coup_o):
        if res_manche == -1:
            if coup_o == PIERRE:
                print('Pierre bat Ciseaux :', score)
            elif coup_o == FEUILLE:
                print('Feuille bat Pierre :', score)
            elif coup_o == CISEAUX:
                print('Ciseaux bat Feuille :', score)
        elif res_manche == 0:
            if coup_o == PIERRE:
                print('Pierre annule Pierre :', score)
            elif coup_o == FEUILLE:
                print('Feuille annule Feuille :', score)
            elif coup_o == CISEAUX:
                print('Ciseaux annule Ciseaux :', score)
        elif res_manche == 1:
            if coup_o == PIERRE:
                print('Pierre est battu par Feuille :', score)
            elif coup_o == FEUILLE:
                print('Feuille est battu par Ciseaux :', score)
            elif coup_o == CISEAUX:
                print('Ciseaux est battu par Pierre :', score)
        return



s = int(input())
random.seed(s)
score = 0

for i in range(5):
    coup_o = random.randint(0, 2)
    coup_j = int(input())
    res_manche = bat(coup_o, coup_j)
    score = score + res_manche
    manche(coup_o)

if score < 0:
    print('Perdu')
elif score >0:
    print('Gagné')
else:
    print('Nul')