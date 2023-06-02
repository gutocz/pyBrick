import random
import turtle

# Setup Screen
wn = turtle.Screen()
wn.title("Brick Destroyer")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # Stops window from updating, speeds up game

# Setup Top Title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 260)
title.write("Brick Destroyer", align="center", font=("Courier", 24, "normal"))

# Setup Screen Border
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.hideturtle()
border.goto(-390, -290)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(780)
    border.lt(90)

# Setup Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Setup Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Setup Brick
brick = turtle.Turtle()
brick.speed(0)
brick.shape("square")
brick.color("white")
brick.penup()
brick.goto(0, 0)

# Setup Bricks in Superior Row
for i in range(5):
    brick.goto(-350 + i * 150, 200)
    brick.stamp()

# Setup Bricks in Middle Row
for i in range(5):
    brick.goto(-350 + i * 150, 200)
    brick.stamp()

# Setup Bricks in Inferior Row
for i in range(5):
    brick.goto(-350 + i * 150, 0)
    brick.stamp()

# Setup Score
score = 0

# Setup Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 230)
scoreboard.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Setup Ball Movement
ball.dx = 0.5
ball.dy = 0.5

# Setup Paddle Movement
def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)

# Setup Keyboard Binding
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# Add Paddle colision with border
def paddle_border():
    if paddle.xcor() > 350:
        paddle.setx(350)
    
    if paddle.xcor() < -350:
        paddle.setx(-350)

# Add colision detection
def isCollision(t1, t2):
    if t1.distance(t2) < 40:
        return True
    else:
        return False
    
# Add Game Over
gameover = turtle.Turtle()
gameover.speed(0)
gameover.color("white")
gameover.penup()
gameover.hideturtle()
gameover.goto(0, 0)

# Add Game Over Message
def game_over():
    gameover.write("GAME OVER\nPLAY AGAIN? (PRESS SPACE)", align="center", font=("Courier", 24, "normal"))
    if wn.onkeypress(reset_game, "space"):
        reset_game()

# Add Reset Game
def reset_game():
    gameover.clear()
    ball.goto(random.randint(-200, 200), random.randint(-200, 200))
    ball.dx *= -1
    ball.dy *= -1

# Aply colision to ball
while True:
    wn.update() # Everytime loop runs, update screen

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Add Border Colision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        game_over()
    
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    
    # Add Paddle Colision
    if isCollision(ball, paddle):
        ball.sety(paddle.ycor() + 30)
        ball.dy *= -1
    
    # Add Brick Colision
    # Add Paddle Border
    paddle_border()

# Main Game Loop
while True:
    wn.update() # Everytime loop runs, update screen