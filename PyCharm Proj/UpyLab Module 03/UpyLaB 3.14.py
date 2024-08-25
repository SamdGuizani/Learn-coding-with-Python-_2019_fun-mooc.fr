import random
NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)

victoire = False
i = 1

while i <= NB_ESSAIS_MAX and victoire is False:
    pari = int(input())
    if pari == secret:
        print('Gagné en ', i, ' essais !')
        victoire = True
    elif pari < secret and i < NB_ESSAIS_MAX:
        print('Trop petit')
    elif pari > secret and i < NB_ESSAIS_MAX:
        print('Trop grand')
    i += 1


if victoire is False:
    print('Perdu ! Le secret était ', secret)

