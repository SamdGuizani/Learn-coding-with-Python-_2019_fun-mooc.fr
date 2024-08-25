"""Projet Vasarely (version 01)
 Auteur : James Bond 007
 Date : 21 Octobre 2019
 Ce programme permet de dessiner un pavage formé de pavés hexagonaux régulièrement espacés.
 Le pavage peut être déformé par une sphère.
 Les variables d'entrée sont :
    inf_gauche = Pavage : Position du coin inférieur gauche
    sup_droit = Pavage : Position du coin supérieur droit
    longueur = Pavage : Longueur du centre du pavé à chaque sommet de l'hexagone avant déformation
    col1 = Pavage : Couleur 1
    col2 = Pavage : Couleur 2
    col3 = Pavage : Couleur 3
    xc = Sphère de déformation : coordonnée x du centre de la sphère de déformation
    yc = Sphère de déformation : coordonnée y du centre de la sphère de déformation
    zc = Sphère de déformation : coordonnée z du centre de la sphère de déformation
    r = Sphère de déformation : rayon de la sphère
 Résultat : Affichage, grâce au module Turtle, d'un joli pavage déformé avec une illusion de 3D
  """


# Importation Modules
import turtle
import math


# Constantes globales
# Section vide


# Définition fonctions
def hexagone(point, longueur, col, centre, rayon):
    """Fonction hexagone : permet de dessiner un pavé hexagonal en joignant 3 losanges.
     Les losange peuvent être déformés par l'introduction d'une sphère.
     Les variables d'entrée sont :
        point = coordonnées du centre du pavé hexagonal sous forme d'un tuple (x, y, 0).
        longueur = Pavage : Longueur du centre du pavé à chaque sommet de l'hexagone avant déformation
        col = tuple de 3 chaines de caractères désignant les couleurs de 3 losanges
        centre = Sphère de déformation : position du centre sous forme de tuple (x, y, z)
        rayon = Sphère de déformation : rayon de la sphère
     Résultat : affichage d'un pavé hexagonal divisé en 3 losanges accolés et déformés"""
    (x0, y0, z0) = point
    (col1, col2, col3) = col

    # Coordonnées sommets du pavé hexagonal avant déformation
    s = []  # Liste des sommets
    for i in range(6):
        s.append((x0 + longueur * math.cos(i * 60 * math.pi / 180),
                  y0 + longueur * math.sin(i * 60 * math.pi / 180),
                  0))

    # Liste de points à déformer
    s.insert(0, point)  # Point central ajouté à la liste des sommets
    pts_av_def = s

    # Liste de points après déformation
    pts_ap_def = []
    for p in pts_av_def:
        p_def = deformation(p, centre, rayon)
        pts_ap_def = pts_ap_def + [p_def]

    # Placer la tortue au centre du pavé
    turtle.up()
    turtle.goto(pts_ap_def[0][0], pts_ap_def[0][1])

    # Tracés des 3 losanges
    for k in range(3):
        turtle.color(col[k], col[k])
        turtle.begin_fill()
        turtle.down()
        if k == 0:
            for i in [1, 6, 5, 0]:
                turtle.goto(pts_ap_def[i][0], pts_ap_def[i][1])  # Traçage 1er losange (en bas, à droite)
        elif k == 1:
            for i in [3, 4, 5, 0]:
                turtle.goto(pts_ap_def[i][0], pts_ap_def[i][1])  # Traçage 2eme losange (à gauche)
        elif k == 2:
            for i in [1, 2, 3, 0]:
                turtle.goto(pts_ap_def[i][0], pts_ap_def[i][1])  # Traçage 3eme losange (en haut, à droite)
        turtle.end_fill()
        turtle.up()
    return


def deformation(p, centre, rayon):
    """Cette fonction a été copiée depuis le site FUN-MOOC, Apprendre à coder en Python (ULB).
    Calcul des coordonnées d'un point suite à la déformation engendrée par la sphère émergeante
        Entrées :
          p : coordonnées (x, y, z) du point du dalage à tracer (z = 0) AVANT déformation
          centre : coordonnées (X0, Y0, Z0) du centre de la sphère (-rayon <= Z0 <= 0)
          rayon : rayon de la sphère
        Sorties : coordonnées (xprim, yprim) du point du dallage à tracer APRÈS déformation
    """
    x, y, z = p
    xprim, yprim, zprim = x, y, z
    xc, yc, zc = centre
    if rayon**2 > zc**2:
        r = math.sqrt(
            (x - xc) ** 2 + (y - yc) ** 2)                  # distance horizontale depuis le point à dessiner jusqu'à l'axe de la sphère
        rayon_emerge = math.sqrt(rayon ** 2 - zc ** 2)           # rayon de la partie émergée de la sphère
        rprim = rayon * math.sin(math.acos(-zc / rayon) * r / rayon_emerge)
        if 0 < r <= rayon_emerge:                 # calcul de la déformation dans les autres cas
            xprim = xc + (x - xc) * rprim / r               # les nouvelles coordonnées sont proportionnelles aux anciennes
            yprim = yc + (y - yc) * rprim / r
        if r <= rayon_emerge:
            beta = math.asin(rprim / rayon)
            zprim = zc + rayon * math.cos(beta)
            if zc > 0:
                zprim *= -1
    return (xprim, yprim, zprim)


def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """Fonction pavage : permet de dessiner un pavage régulier formé de pavés hexagonaux contigus.
    Par construction, le pas horizontal (= distance horizontale entre centres de 2 pavés consécutifs) vaut 3 fois
    la longueur du centre du pavé aux sommets. Le pas vertical (= distance vertical entre centre de 2 pavés contigus
    vaut sqrt(3) * longueur du centre du pavé aux sommets.
    Variables d'entrée :
        inf_gauche = Pavage : Position du coin inférieur gauche
        sup_droit = Pavage : Position du coin supérieur droit
        longueur = Pavage : Longueur du centre du pavé à chaque sommet de l'hexagone avant déformation
        col = Pavage : tuple de 3 couleurs (Couleur 1, Couleur 2, Couleur 3)
        centre = Sphère de déformation : position du centre sous forme de tuple (x, y, z)
        rayon = Sphère de déformation : rayon de la sphère
    Résultat : dessine par itération les pavés en commençant au coin inférieur gauche et terminant au coin supérieur
    droit. La fonction commence par tracer les pavés des lignes paires (0, 2, 4...) puis complète le pavage en traçant
    les pavés des lignes impaires (1, 3, 5...)."""

    a = 3 * longueur  # Pas horizontal pavage (= distance entre centres de 2 pavés consécutifs sur la même ligne)
    b = math.sqrt(3) * longueur  # Pas vertical pavage

    z = 0  # Initialisation coord. z du centre du 1er pavé

    # Traçage pavage lignes pairs
    y = inf_gauche  # Initialisation coord. y du centre du 1er pavé
    while y <= sup_droit:
        x = inf_gauche  # Initialisation coord. x du centre du 1er pavé
        while x <= sup_droit:
            hexagone((x, y, z), longueur, col, centre, rayon)
            x += a
        y += b

    # Traçage pavage lignes impairs
    y = inf_gauche + b / 2  # Initialisation coord. y du centre du 1er pavé
    while y <= sup_droit:
        x = inf_gauche + a / 2  # Initialisation coord. x du centre du 1er pavé
        while x <= sup_droit:
            hexagone((x, y, z), longueur, col, centre, rayon)
            x += a
        y += b
    return


# Code principal
turtle.hideturtle()
turtle.speed(0)

inf_gauche = int(input('Pavage : Position du point inférieur gauche : '))
sup_droit = int(input('Pavage : Position du point supérieur droit : '))
longueur = int(input('Pavage : Longueur du centre du pavage aux sommets avant déformation : '))
col1 = input('Pavage : Couleur 1 : ')
col2 = input('Pavage : Couleur 2 : ')
col3 = input('Pavage : Couleur 3 : ')
xc = int(input('Sphère de déformation : coordonnée x du centre : '))
yc = int(input('Sphère de déformation : coordonnée y du centre : '))
zc = int(input('Sphère de déformation : coordonnée z du centre : '))
r = int(input('Sphère de déformation : rayon de la sphère : '))

pavage(inf_gauche, sup_droit, longueur, (col1, col2, col3), (xc, yc, zc), r)

'''# Paramètres pour test du programme :
inf_gauche = -300
sup_droit = 300
longueur = 10
col1 = 'dark red'
col2 = 'black'
col3 = 'coral'
centre = (-50, -50, -50)
r = 230

pavage(inf_gauche, sup_droit, longueur, (col1, col2, col3), centre, r)'''

turtle.getcanvas().postscript(file="pavage.eps")
turtle.exitonclick()
