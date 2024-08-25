import random
secret = random.randint(1, 5)
pari = int(input('Devinez le nombre secret : '))

if pari == secret:
    print('Bravo ! Vous avez deviné le nombre secret.')
else:
    print('Perdu ! La valeur était ', secret)