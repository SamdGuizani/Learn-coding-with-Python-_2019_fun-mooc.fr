x = 0
n = 0
somme = 0

while x != -1:
    x = int(input())  # Nb salariées de l'entreprise, -1 signifie fin des entrées
    somme = somme + x  # Nb totale de salariées
    n = n + 1  # Nb d'entreprises
    #  print(x, somme, n)
    if x == -1:
        n = n - 1
        somme = somme + 1
        #  print (x, somme, n)
moyenne = somme / n
print(moyenne)