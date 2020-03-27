import turtle
import socket
host = socket.gethostbyname(socket.gethostname())
port = 9996
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(True)
def client1_send(data, s):
    server = ("192.168.1.4", 9090)
    s.sendto(data.encode(), server)
client1_send("[Client join//", s)

wn = turtle.Screen()
wn.bgcolor('black')
wn.title("PingPong")
wn.setup(height=600, width=600)

#Score!!!
score_a = 0
score_b = 0

#pen for write
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Your Score: 0  Opponent: 0", align="center", font=("Courier",24,"normal"))

paddleLeft = turtle.Turtle()
paddleLeft.speed(0)
paddleLeft.shape("square")
paddleLeft.color("white")
paddleLeft.shapesize(stretch_wid=7, stretch_len=1)
paddleLeft.penup()
paddleLeft.goto(-250, 0)

def paddleLeft_up():
    y = paddleLeft.ycor()
    y += 20
    paddleLeft.sety(y)

def paddleLeft_down():
    y = paddleLeft.ycor()
    y -= 20
    paddleLeft.sety(y)

wn.listen()
wn.onkeypress(paddleLeft_up, "w")
wn.onkeypress(paddleLeft_down, "s")

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3
play = True
while True:
    if play:
        wn.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        if ball.ycor() > 290:  #  Y +
            ball.sety(290)
            ball.dy = ball.dy * -1
        if ball.ycor() < -290:  #  Y -
            ball.sety(-290)
            ball.dy = ball.dy * -1
        if ball.xcor() > 390:  #  X +
            client1_send("left/"+str(ball.xcor())+"/"+str(ball.ycor())+"/"+str(ball.dx)+"/"+str(ball.dy)+'/'+str(score_a)+'/'+str(score_b),s)
            play = False
            pen.clear()
            pen.write(f"Your Score: {score_a}  Opponent: {score_b}", align="center", font=("Courier", 24, "normal"))
        if ball.xcor() < -390:  # X -
            ball.goto(0, 0)
            ball.dx = ball.dx * -1
            score_b += 1
            pen.clear()
            pen.write(f"Your Score: {score_a}  Opponent: {score_b}", align="center", font=("Courier", 24, "normal"))
        if (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < paddleLeft.ycor() + 40 and ball.ycor() > paddleLeft.ycor() - 40):
            ball.setx(-240)
            ball.dx = ball.dx * -1
        if paddleLeft.ycor() > 260:
            paddleLeft.sety(260)
        if paddleLeft.ycor() < -260:
            paddleLeft.sety(-260)
    else:
        data, addr = s.recvfrom(1024)
        ballInfo = str(data.decode()).split('/')
        if ballInfo[0] == "right":
            ball.setx(-1*int(ballInfo[1]))
            ball.sety(int(ballInfo[2]))
            ball.dx = int(ballInfo[3])
            ball.dy = int(ballInfo[4])
            score_a = int(ballInfo[5])
            score_b = int(ballInfo[6])
            pen.clear()
            pen.write(f"Your Score: {score_b}  Opponent: {score_a}", align="center", font=("Courier", 24, "normal"))
            play = True
            print("received ball: "+str(data.decode()))
wn.mainloop()
s.close()