import turtle
import random


window = turtle.Screen()
window.title("My Window of Ball Game")
window.bgcolor("black")
window.setup(width=800, height=800)
window.tracer(1)


score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.color("white")
pen.write("Score:0", align="center", font=("Courier", 24, "normal"))


player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.shapesize(stretch_wid=2, stretch_len=5)
player.penup()
player.goto(0, -250)


window.mainloop()
