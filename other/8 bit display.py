from turtle import *
from time import sleep

def drawHexLong():
    forward(30)
    right(45)
    forward(10)
    right(90)
    forward(10)
    right(45)
    forward(60)
    right(45)
    forward(10)
    right(90)
    forward(10)
    right(45)
    forward(30)

location = [[0,50,0], [51.2, 1.2, 90], [51.2,-87.1, 0], [0,-138.2, 90], [-51.2,-87.1, 90], [-51.2, 1.2, 0], [0, -35.9, 90]]

def drawNum(inputNumber):
    for i in range(len(location)):
        goto(location[i][0], location[i][1])
        right(location[i][2])
        down()
        if inputNumber[i] ==  "1":
            fillcolor("black")
        else:
            fillcolor("white")
        begin_fill()
        drawHexLong()
        end_fill()
        up()
    goto(0,0)

up()

write = ["0110111", "1001111", "0001110", "0001110", "1111110", "0001000", "1110110", "1001111", "0111110", "1111110"]

while True:
    for i in range(len(write)):
        tracer(0)
        drawNum(write[i])
        tracer(1)
        sleep(1)

