from numpy import *

def conjugate(dual):
    return (dual[0], -dual[1])
def square(dual):
    return (dual[0]**2, 2*dual[0]*dual[1])
def add(dual, dualToAdd, negate=1):
    return (dual[0] + (dualToAdd[0]*negate), dual[1] + (dualToAdd[1]*negate))
def multiply(dual, dualToMultiply):
    return (dual[0]*dualToMultiply[0], dual[0]*dualToMultiply[1] + dual[1]*dualToMultiply[0])
def division(dual, dualToDivide):
    tempDual = multiply(dual, conjugate(dualToDivide))
    return (tempDual[0]/(dualToDivide[0]**2), tempDual[1]/(dualToDivide[0]**2))
def display(dual):
    return f"{dual[0]} + {dual[1]}ε"
def absolute(dual):
    return (abs(dual[0])**2 + abs(dual[1]**2))**1/2
def argument(dual):
    if real(dual[0]) != dual[0] or real(dual[1]) != dual[1]:
        return ValueError
    if dual[0] == 0:
        if dual[1] > 0:
            return pi/2
        return -pi/2
    return atan(dual[1]/dual[0])
