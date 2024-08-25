"""
Project Vasarely
Auteur: mchretie 000498327
Date: 27/10/19
Programme dédier à creer un pavage insperer de Mr. Vasarely
Input: Limite du pavage, taille des hexagones,
        3 couleurs des 3 faces, centre et rayon de la sphère
Output: oeuvre visuel
"""
import turtle                                        #import module turtle

from deformation import deformation                  #import fonction déformation

def hexagone(point, longueur, col, centre, rayon):
    """lecture des valeurs, calcul de chaque point,
     pour tracer un poligone précis"""

    dist = list(point)

    m = [0, 0, 0]
    l = [0, 0, 0]
    k = [0, 0, 0]
    j = [0, 0, 0]
    h = [0, 0, 0]
    g = [0, 0, 0]

    m[:] = dist
    m[0] += longueur
    l[:] = dist
    l[0] += (longueur / 2)
    l[1] += pytha
    k[:] = l
    k[0] -= longueur
    j[:] = dist
    j[0] -= longueur
    h[:] = k
    h[1] -= 2 * pytha
    g[:] = h
    g[0] += longueur
    g = deformation(g, centre, rayon)
    h = deformation(h, centre, rayon)
    j = deformation(j, centre, rayon)
    k = deformation(k, centre, rayon)
    l = deformation(l, centre, rayon)
    m = deformation(m, centre, rayon)
    point = deformation(point, centre, rayon)

    turtle.speed(0)
    turtle.up()
    turtle.goto(point[:2])
    turtle.down()

    turtle.color(col[0])  #premier parallelogramme
    turtle.begin_fill()
    turtle.goto(m[:2])
    turtle.goto(l[:2])
    turtle.goto(k[:2])
    turtle.goto(point[:2])
    turtle.end_fill()

    turtle.color(col[1]) #2e parallelo
    turtle.begin_fill()
    turtle.goto(k[:2])
    turtle.goto(j[:2])
    turtle.goto(h[:2])
    turtle.goto(point[:2])
    turtle.end_fill()


    turtle.color(col[2])  # 3e parallelo
    turtle.begin_fill()
    turtle.goto(m[:2])
    turtle.goto(g[:2])
    turtle.goto(h[:2])
    turtle.end_fill()



def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """dirige le placement des poligones """
    point = list(inf_gauche)
    i = 0
    point.append(0)


    while point[1] < sup_droit[1]:

        while point[0] < sup_droit[0]:
            hexagone(point, longueur, col, centre, rayon)
            point[0] += 3*longueur
        point[1] += pytha
        point[0] = inf_gauche[0]
        i += 1
        point[0] += (i%2)*longueur*1.5

    turtle.done()

#paramettres d'entrée
inf_gauche = (-300, -300)       #bornes
sup_droit = (300, 300)
longueur = 50                   #taille d'une arête
col = ('blue', 'black', 'red')  #couleurs des faces
centre = (-50, -50, 0)         #milieu sphère
rayon = 240                     #rayon de le sphère

# distance entre centre et milieu d'une arête, utilisé dans fonction pavage et hexagone
pytha = ((longueur ** 2) - ((longueur / 2) ** 2)) ** 0.5

pavage(inf_gauche, sup_droit, longueur, col, centre, rayon)

