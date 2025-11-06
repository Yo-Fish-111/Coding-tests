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

def drawHexHalf():
    forward(27)
    right(45)
    forward(10)
    right(90)
    forward(10)
    right(45)
    forward(27)
    right(90)
    forward(14.1)
    right(90)

def drawDiagHex():
    forward(8.3)
    left(74.8)
    forward(40)
    left(15.2)
    forward(19.2)
    left(90)
    forward(8.3)
    left(74.8)
    forward(40)
    left(15.2)
    forward(19.2)
    left(90)



def drawNumPart(inputNumber, j):
    for i in range(6):
        goto(location[i][0], location[i][1])
        right(location[i][2])
        down()
        if inputNumber[i] ==  "1":
            fillcolor(colours[j])
            j+=1
        else:
            fillcolor((0,0,0))
        if j == len(colours):
            j = 0
        begin_fill()
        drawHexLong()
        end_fill()
        up()
    goto(0,0)

def drawNumMore(inputNumber, j):
    for i in range(6,8):
        goto(location[i][0], location[i][1])
        right(location[i][2])
        down()
        if inputNumber[i] == "1":
            fillcolor(colours[j])
            j += 1
        else:
            fillcolor((0, 0, 0))
        if j == len(colours):
            j = 0
        begin_fill()
        drawHexHalf()
        end_fill()
        up()
    right(180)

def drawNumYetMore(inputNumber, j):
    for i in range(8,10):
        goto(location[i][0], location[i][1])
        right(location[i][2])
        down()
        if inputNumber[i] == "1":
            tracer(0)
            fillcolor(colours[j])
            j += 1
        else:
            fillcolor((0, 0, 0))
        if j == len(colours):
            j = 0
        begin_fill()
        drawDiagHex()
        end_fill()
        up()


location = [[0,50,0], [51.2, 1.2, 90], [51.2,-87.1, 0], [0,-138.2, 90], [-51.2,-87.1, 90], [-51.2, 1.2, 0], [3, -35.9, 90], [-3,-50.1, 180], [3, -32, 0], [-41.2, -128.2, 0]]
colours = [(96, 208, 250), (245, 172, 186), (255,255,255), (245, 172, 186), (96, 208, 250)]




up()
write = ["1011111000", "1111110000", "1111110000", "1111100001"]
#hideturtle()
colormode(255)
bgcolor((0,0,0))
pencolor((255,255,255))

j = 0





while True:
    for i in range(len(write)):
        tracer(0)
        drawNumPart(write[i], j)
        drawNumMore(write[i], j)
        drawNumYetMore(write[i], j)
        tracer(1)
        sleep(1)

tracer(1)
drawNumYetMore(write[1], j)
sleep(10)
