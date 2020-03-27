import turtle
# PinPong_BaseCanvas

#Canvas
win = turtle.Screen()
win.bgcolor("black")
win.title("PinPong")
win.setup(1200, 600)
win.tracer(0)

#Shapes
# Left Player
racket_left = turtle.Turtle()
racket_left.shape("square")
racket_left.color("white")
racket_left.speed(0)
racket_left.shapesize(stretch_len=0.8, stretch_wid= 5)
racket_left.penup()
racket_left.goto(-550, 0)


# Right Player

racket_right = turtle.Turtle()
racket_right.shape("square")
racket_right.color("white")
racket_right.speed(0)
racket_right.shapesize(stretch_len=0.8, stretch_wid= 5)
racket_right.penup()
racket_right.goto(550, 0)


#Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.goto(0,0)
ball.penup()
ball.shapesize(1, 1)
ball.color("white")
ball.dx = 0.3
ball.dy = 0.3

#Text
score = turtle.Turtle()
score.goto(0, 260)
score.speed(0)
score.penup()
score.color("white")
score. hideturtle()
pR = 0
Pl = 0



def Restart_BTN():
    ball.goto(0, 0)
    racket_left.goto(-550, 0)
    racket_right.goto(550, 0)
    pause_block = turtle.Turtle
    pause_block.penup()
    pause_block.color("white")
    pause_block.shape("square")
    pause_block.shapesize(stretch_len=5, stretch_wid= 5)



score.write("Player 1 : {}            ||     ||          Player 2 : {} ".format(Pl, pR), align='center', font=('System', 22, "bold"))

#racket_move
def racket_move_up():
    y = racket_left.ycor()
    y += 30
    racket_left.sety(y)
def racket_move_down():
    y = racket_left.ycor()
    y -= 30
    racket_left.sety(y)

def racket_move_up1():
    y = racket_right.ycor()
    y += 30
    racket_right.sety(y)
def racket_move_down1():
    y = racket_right.ycor()
    y -= 30
    racket_right.sety(y)

win.listen()
win.onkeypress(racket_move_up, "w")
win.onkeypress(racket_move_down, "s")

win.onkeypress(racket_move_up1, "Up")
win.onkeypress(racket_move_down1, "Down")

win.onkeypress(Restart_BTN, "space")

while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 590:
        ball.goto(0, 0)
        ball.dx *= -1
        Pl += 1
        score.clear()
        score.write("Player 1 : {}            ||     ||          Player 2 : {} ".format(Pl, pR), align='center',font=('System', 22, "bold"))

    if ball.xcor() < -590:
        ball.goto(0, 0)
        ball.dx *= -1
        pR += 1
        score.clear()
        score.write("Player 1 : {}            ||     ||          Player 2 : {} ".format(Pl, pR), align='center', font=('System', 22, "bold"))

    if ball.xcor() > 540 and ball.ycor() < racket_right .ycor() + 50 and ball.ycor() > racket_right.ycor() - 50:
        ball.dx *= -1

    if ball.xcor() < -540 and ball.ycor() < racket_left .ycor() + 50 and ball.ycor() > racket_left.ycor() - 50:
        ball.dx *= -1

    if racket_left.ycor() > 290:
        racket_left.goto(-550, 280)

    if racket_left.ycor() < -290:
        racket_left.goto(-550, -280)

    if racket_right.ycor() > 290:
        racket_right.goto(550, 280)

    if racket_right.ycor() < -290:
        racket_right.goto(550, -280)
    win.update()