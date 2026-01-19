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


ball = turtle.Turtle()

ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(random.randint(-280, 280), 250)
ball_speed = 5 * 1.10


def move_left():
    x = player.xcor() - 20
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor() + 20
    if x > 280:
        x = 280
    player.setx(x)


def game_loop():
    global score, ball_speed
    ball.sety(ball.ycor() - ball_speed)

    if (player.xcor() - 50 < ball.xcor() < player.xcor() + 50) and (
        player.xcor() - 50 < ball.xcor() < player.xcor() + 50
    ):
        score += 1
        ball_speed *= 1.01
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
        ball.goto(random.randint(-280, 280), 250)

    if ball.ycor() < -300:
        pen.clear()
        pen.goto(0, 0)
        pen.write(
            "Game Over | Press R to Restart",
            align="center",
            font=("Courier", 24, "normal"),
        )
        return
    window.update()
    window.ontimer(game_loop, 30)


window.listen()
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

game_loop()
window.mainloop()
