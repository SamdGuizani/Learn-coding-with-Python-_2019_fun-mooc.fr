import turtle

"""Dessine un polygone régulier à n côtés de longueur l"""

n = int(input('Nombre de côtés du polygone régulier à dessiner : '))
l = float(input('Longueur du côté : '))
for i in range(n):
    turtle.forward(l)
    turtle.left(360/n)
turtle.exitonclick()
