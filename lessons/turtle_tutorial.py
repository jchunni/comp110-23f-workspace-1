"""Turtle tutorial"""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.penup()
leo.goto(-150, -100)
leo.pendown()

leo.speed(50)
leo.hideturtle()

leo.begin_fill()
leo.color(38, 99, 80)


i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
done()






