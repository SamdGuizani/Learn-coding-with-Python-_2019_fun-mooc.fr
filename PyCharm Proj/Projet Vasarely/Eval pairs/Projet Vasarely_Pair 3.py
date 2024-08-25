"""
PROJET VASALERY : faire un programme python produisant des tableaux d'art optique
Auteur : Mvukiyehe Ishimwe Melissa
N° de matricule : 000494471
Date : 27 septembre 2019
"""
import turtle
from math import pi , cos , sin
from deformation import deformation
""" Calcul des coordonnées d'un point suite à la déformation engendrée par la sphère émergeante
        Entrées :
          p : coordonnées (x, y, z) du point du dalage à tracer (z = 0) AVANT déformation
          centre : coordonnées (X0, Y0, Z0) du centre de la sphère
          rayon : rayon de la sphère
        Sorties : coordonnées (xprim, yprim, zprim) du point du dallage à tracer APRÈS déformation
"""
def hexagone(point, col , longueur , centre , rayon ) :
    """
    :param point: point du centre de mon hexagone avant déformation
    :param col: couleur de chaque face de mon hexagone
    :param longueur: rayon de l'hexagone par rapport au centre
    :param centre: centre du cercle de déformation
    :param rayon: rayon du cercle de déformation
    """
    a,b,c= point
    pt = (deformation((a,b,c),centre,rayon )[0], deformation((a,b,c),centre,rayon)[1],0)
    x , y, Z = pt #valeur de mon point après déformation
    COL1, COL2, COL3 = col
    for FACE in range (3) :    #La création de nos 3faces de notre hexagone
        if FACE  ==0 :         #Condition pour avoir la 1er , 2eme et 3eme face
            turtle.color(COL1)
            s = 4*pi / 3
        if FACE  == 1 :
            turtle.color(COL2)
            s= 2*pi / 3
        if FACE == 2 :
            turtle.color(COL3)
            s = 2*pi
        turtle.begin_fill()

        turtle.up()
        turtle.goto(x,y)
        turtle.down()

        x_1 = longueur * cos(s) + a
        y_1 = longueur * sin(s) + b
        A = (deformation((x_1,y_1,Z), centre , rayon)[0], (deformation((x_1,y_1,Z), centre , rayon)[1]),0)
        x_1 , y_1 , Z = A
        turtle.goto( x_1 , y_1 )

        x_2 = longueur*cos(s - pi/3) + a
        y_2 =  longueur*sin(s - pi/3) + b
        B = (deformation((x_2,y_2,Z),centre,rayon)[0], (deformation((x_2,y_2,Z),centre,rayon)[1]),0)
        x_2 , y_2 , Z = B
        turtle.goto(x_2 , y_2)

        x_3 = longueur* cos(s-2*(pi/3)) + a
        y_3 = longueur * sin(s - 2*(pi/3)) + b
        C = (deformation((x_3,y_3,Z),centre,rayon)[0],deformation((x_3,y_3,Z),centre,rayon)[1],0)
        x_3,y_3,Z = C
        turtle.goto(x_3, y_3)

        turtle.goto(x,y)
        turtle.end_fill()
        turtle.hideturtle()

def pavage(inf_gauche , sup_droit , longueur , col , centre , rayon ) :
    """
    :param inf_gauche: centre d'hexagone le plus bas à gauche
    :param sup_droit:  centre d'hesagone le plus haut à droite
    """
    x_4 = inf_gauche
    y_4= x_4
    x_5= sup_droit
    y_5= x_5
    Z = 0
    a , b , c = centre
    Nombre_de_ligne = 0
    point = (x_4 , y_4 , Z)
    while y_4 < y_5 :
        n = 0
        while x_4 < x_5:      #Permet de faire une ligne d'hexagone
            hexagone( point ,col , longueur, centre, rayon )
            x_4 += 3* longueur
            point = x_4 , y_4 , Z
            n += 3
        Nombre_de_ligne+=1
        if Nombre_de_ligne % 2 !=0 : #Permet de faire ma ligne impaire
            x_4 += longueur * ((3/2) - n  )
            y_4  +=  longueur *cos(pi/6)
            point = x_4 , y_4 , Z
        else  :                      #Permet de faire ma ligne paire
            x_4  -= (n + 3/2) * longueur
            y_4 += longueur * cos(pi/6)
            point = x_4 , y_4 , Z
    turtle.done()

#Code principal
turtle.tracer(100)
inf_gauche = int(input())
sup_droit = int(input())
longueur = int(input())
COL1 = input()
COL2 = input()
COL3 = input()
col = COL1,COL2, COL3
a = int(input())
b = int(input())
c = int(input())
centre = a, b, c
rayon = int(input())
pavage(inf_gauche , sup_droit , longueur , col , centre , rayon )










