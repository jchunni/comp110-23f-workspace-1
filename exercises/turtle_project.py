"""Turtle Project!"""

__author__ = "730475774"

from turtle import Turtle, colormode, done
colormode(255)
scene: Turtle = Turtle()


def draw_sky(scene: Turtle, x: int, y: int) -> None:
    """This function will create the sky of the scene by starting in the very top left corner and filling in the top of the screen with dark purple."""
    scene.begin_fill()
    scene.color(21, 43, 90)
    scene.penup()
    scene.goto(x, y)
    scene.pendown
    scene.forward(800)
    scene.right(90)
    scene.forward(400)
    scene.right(90)
    scene.forward(800)
    scene.right(90)
    scene.forward(400)
    scene.end_fill()


def draw_star(scene: Turtle, x: int, y: int) -> None:
    """This function will create a yellow star wherever the user designates the x,y coordinates to be using a loop."""
    scene.begin_fill()
    scene.color(228, 226, 132)
    scene.penup()
    scene.goto(x, y)
    scene.setheading(0.0)
    scene.pendown()
    i: int = 0
    while i < 5:
        scene.forward(80)
        scene.left(144)
        i = i + 1
    scene.end_fill()


def draw_bird(scene: Turtle, x: int, y: int) -> None:
    """This function will create smnall brown birds, wherever the user designates the x,y coordinates to be."""
    scene.color("brown")
    scene.penup()
    scene.goto(x, y)
    scene.setheading(0.0)
    scene.pendown()
    scene.forward(20)
    scene.right(20)
    scene.forward(30)
    scene.left(40)
    scene.forward(30)
    scene.right(20)
    scene.forward(20)


def draw_ground(scene: Turtle, x: int, y: int) -> None:
    """This function puts into place a green rectangle which is meant to depict the ground of the scene where the user designates the x,y coordinates to be."""
    scene.begin_fill()
    scene.color(161, 212, 114)
    scene.penup()
    scene.goto(x, y)
    scene.setheading(0.0)
    scene.pendown()
    scene.forward(800)
    scene.right(90)
    scene.forward(400)
    scene.right(90)
    scene.forward(800)
    scene.right(90)
    scene.forward(400)
    scene.end_fill()


def draw_grass(scene: Turtle, x: int, y: int) -> None:
    """This function creates zig zags that allows for more dimension wherever the user places it using the x,y coordinates."""
    scene.pencolor(106, 144, 72)
    scene.penup()
    scene.setheading(0.0)
    scene.goto(x, y)
    scene.pendown()
    i: int = 0
    while i < 3:
        scene.right(30)
        scene.forward(20)
        scene.left(30)
        scene.forward(20)
        i = i + 1


def draw_lake(scene: Turtle, x: int, y: int) -> None:
    """This function will draw a small, blue, round lake wherever the user designates the coordinates the x,y coordinates to be."""
    scene.begin_fill()
    scene.color(144, 204, 242)
    scene.penup()
    scene.goto(x, y)
    scene.setheading(0.0)
    scene.pendown
    scene.circle(120)
    scene.end_fill()


def main() -> None:
    """This is the entirety of the scene put together."""
    scene: Turtle = Turtle()
    draw_sky(scene, -375, 350)
    draw_star(scene, -200, 200)
    draw_star(scene, -100, 150)
    draw_star(scene, 235, 175)
    draw_bird(scene, 100, 40)
    draw_bird(scene, -275, 275)
    draw_ground(scene, -375, 0)
    draw_lake(scene, 0, -260)
    draw_grass(scene, -290, -80)
    draw_grass(scene, -240, -275)
    draw_grass(scene, 225, -205)
    done()


if __name__ == "__main__":
    main()