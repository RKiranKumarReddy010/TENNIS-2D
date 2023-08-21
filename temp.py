import turtle


wn = turtle.Screen()
wn.title("ping pong game")
wn.bgcolor("white")
wn.setup(width=800,height=600)
wn.tracer()

pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
score_a=0
score_b=0

#P  A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#P  B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#BALL
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
    
    


#keyword binding
wn.listen()
wn.onkeypress(paddle_a_up,"1")
wn.onkeypress(paddle_a_down,"2")
wn.onkeypress(paddle_b_up,"9")
wn.onkeypress(paddle_b_down,"0")


while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
    
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1