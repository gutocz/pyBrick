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

# Main Game Loop
while True:
    wn.update() # Everytime loop runs, update screen