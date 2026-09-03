from MassObject import *
from time import time, sleep
from random import randint

lastTick = time()
width = 800
height = 800
win = gr.GraphWin("mainWin", width, height)
win.setBackground("black")


sun = MassObject(Vector(245, 430), 27, 20000, Vector(0, 0), 1)
earth = MassObject(Vector(250, 300), 9, 800, Vector(0, 20), 1)

close = False
massList = []

for i in range(100):
    radius = randint(1, 5)
    massList.append(MassObject(Vector(randint(100,700), randint(100,700)),
                                radius, radius * 100,
                                Vector(randint(-10,10), randint(-10,10))))
    massList[-1].setFill("white")
    massList[-1].draw(win)

while not close:
    dt = time()-lastTick
    lastTick = time()
    close = ("x" == win.checkKey())

    for mass in massList:
        mass.runUpdates(massList, win, dt)
        print(mass)
