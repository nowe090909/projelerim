import turtle
import random

def Cokgen(kenarSayisi, uzunluk, x, y, renk="black", dolgu=False):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.color(renk)
    if dolgu:
        turtle.begin_fill()
    for i in range(kenarSayisi):
        turtle.forward(uzunluk)
        turtle.left(360//kenarSayisi)
    if dolgu:
        turtle.begin_fill()
        turtle.hideturtle()
        turtle.hideturtle()
        turtle.tracer(0)
Cokgen(3, 30, 10, 10)
Cokgen(4, 30, 50, 50, "blue")
Cokgen(5, 30, 100, 100, "red", True)
turtle.update() 
turtle.exitonclick()
