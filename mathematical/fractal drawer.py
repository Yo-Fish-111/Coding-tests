from queueImplementation import *
from turtle import *

hideturtle()
LevelsToAdd = declareQueue(3**10, "LIST")
# [Ogtilt, angle, length, ogLoca, decay, remLevels]
add(LevelsToAdd, [90, 50, 50, (0,0), 3/4, 8])
tracer(0)

while not isEmpty(LevelsToAdd):
    currentLevel = retrieve(LevelsToAdd)
    up()
    goto(currentLevel[3])
    setheading(currentLevel[0])
    down()
    forward(currentLevel[2])
    location = position()
    if currentLevel[5] == 0:
        break
    add(LevelsToAdd, [currentLevel[0]+currentLevel[1], currentLevel[1]*currentLevel[4], currentLevel[2]*currentLevel[4], location, currentLevel[4], currentLevel[5]-1])
    add(LevelsToAdd, [currentLevel[0], currentLevel[1]*currentLevel[4], currentLevel[2]*currentLevel[4], location, currentLevel[4], currentLevel[5]-1])
    add(LevelsToAdd, [currentLevel[0]-currentLevel[1], currentLevel[1]*currentLevel[4], currentLevel[2]*currentLevel[4], location, currentLevel[4], currentLevel[5]-1])
    if peak(LevelsToAdd)[5] == currentLevel[5]-1:
        update()
        input("Press Enter for the next layer")

up()
tracer(1)
while True:
    goto(200,200)

