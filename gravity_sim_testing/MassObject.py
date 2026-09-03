import graphics as gr
from Vector import *
from Force import *


G = 6.6743


class MassObject(gr.Circle):
    mass: int
    velocity: Vector
    position: Vector
    solidity: int
    forces: list[Force]



class MassObject(gr.Circle):
    def __init__(self, start: Vector, radius, mass, velocity=Vector(0, 0), solidity=1):
        self.mass = mass
        self.velocity = velocity
        self.position = start
        super().__init__(start, radius)

        self.solidity = solidity
        self.forces = []


    def __str__(self):
        return f"object at position {self.position}"


    def runUpdates(self, MassList: list[MassObject], canvas: gr.GraphWin, dt):
        self.forces = []
        for otherMass in MassList:
            if otherMass == self: continue
            massVector = otherMass.position - self.position # position Vector from self to otherMass
            self.gravityUpdate(otherMass)
            if massVector.length() < self.radius + otherMass.radius:
                self.collide(otherMass)
        self.update(dt)

    def updatePosition(self, positonChange: Vector):
        self.move(positonChange.x, positonChange.y)
        self.position += positonChange

    def collide(self, otherMass):
        massVector = otherMass.position - self.position
        resultantSolidity = otherMass.solidity * self.solidity
        overlap = self.radius + otherMass.radius - massVector.length()
        forceToApply = self.mass * self.velocity.length() * resultantSolidity * overlap**2 * -massVector / massVector.length()
        #self.forces.append(forceToApply)

    def gravityUpdate(self, otherMass):
        massVector = (otherMass.position - self.position)
        if massVector.length() == 0: return
        massVector.setMag(G * (self.mass * otherMass.mass) / (massVector.length() ** 2))
        forceToApply = makeForce(massVector)
        self.forces.append(forceToApply)


    def update(self, dt):
        resultantForce = Vector(0,0)
        for force in self.forces:
            resultantForce+= force

        acceleration = resultantForce / self.mass
        self.velocity += acceleration * dt

        self.updatePosition(self.velocity * dt)

