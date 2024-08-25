import turtle
import math
import random
import time


def pave(t, abscisse_centre, ordonnee_centre, longueur_arete, color1, color2, color3):
    """ Dessine avec turtle un pave hexagonal
        en position ( abscisse_centre, ordonnee_centre)
        paramètres :
        - t : la turtle,
        - (abscisse_centre, ordonnee_centre) : point centre du pavé
        -  longueur_arete : longueur de chaque arête du pavé
        - color1, color2, color3 : les couleurs des 3 hexagones"""

    # Coordonnées point central
    x0, y0 = abscisse_centre, ordonnee_centre

    # Coordonnées sommets
    x1, y1 = x0 + longueur_arete * math.cos(0 * math.pi / 180), y0 + longueur_arete * math.sin(0 * math.pi / 180)
    x2, y2 = x0 + longueur_arete * math.cos(60 * math.pi / 180), y0 + longueur_arete * math.sin(60 * math.pi / 180)
    x3, y3 = x0 + longueur_arete * math.cos(120 * math.pi / 180), y0 + longueur_arete * math.sin(120 * math.pi / 180)
    x4, y4 = x0 + longueur_arete * math.cos(180 * math.pi / 180), y0 + longueur_arete * math.sin(180 * math.pi / 180)
    x5, y5 = x0 + longueur_arete * math.cos(240 * math.pi / 180), y0 + longueur_arete * math.sin(240 * math.pi / 180)
    x6, y6 = x0 + longueur_arete * math.cos(300 * math.pi / 180), y0 + longueur_arete * math.sin(300 * math.pi / 180)

    # Placer la tortue au centre du pavé
    t.up()
    t.goto(x0, y0)

    # Tracer 1er losange
    t.color(color1, color1)
    t.begin_fill()
    t.down()
    t.goto(x1, y1)
    t.goto(x6, y6)
    t.goto(x5, y5)
    t.goto(x0, y0)
    t.end_fill()
    t.up()

    # Tracer 2eme losange
    t.color(color2, color2)
    t.begin_fill()
    t.down()
    t.goto(x1, y1)
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x0, y0)
    t.end_fill()
    t.up()

    # Tracer 3eme losange
    t.color(color3, color3)
    t.begin_fill()
    t.down()
    t.goto(x3, y3)
    t.goto(x4, y4)
    t.goto(x5, y5)
    t.goto(x0, y0)
    t.end_fill()
    t.up()


turtle.hideturtle()
turtle.speed(0)
turtle.reset()
time.sleep(5)

while True:
    pave(turtle, random.randint(-300,300),  random.randint(-300,300),
        random.randint(10,50), 'black', 'red', 'blue')
    pave(turtle, random.randint(-300,300),  random.randint(-300,300),
        random.randint(10,50), 'white', 'grey', 'black')