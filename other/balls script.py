import turtle
from random import  *
from time import sleep

width = 1150
height = 650
turtle.colormode(255)
turtle.bgcolor((0,0,0))
turtle.pensize(2)
turtle.speed("fastest")
turtle.screensize(width, height)
turtle.tracer(0, 0)

output = open("C:\\data\\codes.txt", "w")

turtle.up()
ballred = 0
ballgreen = 0
ballblue = 0
colours = []

numOfBalls = 20000
colourStep = (15777216 // numOfBalls)

for i in range(numOfBalls):
    ballblue = ballblue + colourStep
    while ballblue > 255:
        ballblue = ballblue - 255
        ballgreen = ballgreen + 1
    while ballgreen > 255:
        ballgreen = ballgreen - 255
        ballred = ballred + 1
    ballscolour = [ballred, ballgreen, ballblue]
    print(ballscolour)
    output.write(str(ballscolour) + "\n")
    colours.append(ballscolour)

print(len(colours))

turtleX = 0
turtleY = 0

for i in range(len(colours)):
    turtle.down()
    turtle.color((int(colours[i][0]), int(colours[i][1]), int(colours[i][2])))
    turtle.forward(1)
    turtle.up()
    turtle.pensize(randint(1,3))
    turtleX= turtleX+randint(-10,10)
    turtleY= turtleY+randint(-10,10)
    while turtleX > width/2:
        turtleX = turtleX-width
    while turtleX < -width/2:
        turtleX = turtleX+width
    while turtleY > height/2:
        turtleY = turtleY-height
    while turtleY < -height/2:
        turtleY = turtleY+height
    print(turtleX,turtleY)
    turtle.goto(turtleX, turtleY)
    print(i)

turtle.update()
turtle.getcanvas().postscript(file="ballsimg.eps")

turtle.tracer(1)

turtleX = width ** 2
while True:
    turtle.goto(width/2,height/2)
