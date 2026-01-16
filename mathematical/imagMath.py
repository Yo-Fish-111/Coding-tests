"""
This module provides access to mathematical functions for Imaginary Objects with abitrary imaginary units
numbers.
"""


# Variables with simple values
e = 2.718281828459045
pi = 3.141592653589793
tau = 6.283185307179586
gamma = 0.577215664901532
phi = 1.618033988749894
apery = 1.202056903159594

imajCount = 0


class imjCoefficient:
    def __init__(self, multTo, symbol):
        global imajCount
        self.position = imajCount
        imajCount+=1
        self.multTo = multTo
        self.symbol = symbol

    def __mul__(self, other):
        if type(other) != imjCoefficient:
            return TypeError
        elif self.multTo == other.multTo:
            return self.multTo
        elif self.position < other.position:
            imajinary = f"{self.symbol}{other.symbol}"
        else:
            imajinary = f"{other.symbol}{self.symbol}"
        return  imjCoefficient(self.multTo * other.multTo, imajinary)
    def __rmul__(self, other):
        if type(other) != imjCoefficient:
            return TypeError
        return other * self


    def __str__(self):
        return str(self.symbol)

class imgObj:
    def __init__(self, real, imagParts=[], coefficients=[]):
        self.real = real
        self.imagParts = imagParts
        self.coefficients = coefficients

    def __str__(self):
        representation = f"{self.real}"
        for i in range(len(self.imagParts)):
            representation = f"{representation} + {self.coefficients[i]}{self.imagParts[i]}"
        return representation

    def __mul__(self, other):
        returnVal = imgObj(0, [],[])
        if type(other) in [int, float]:
            returnVal.real = self.real*other
            for index in range(len(self.coefficients)):
                returnVal.coefficients.append(other * self.coefficients[index])
                returnVal.imagParts.append(self.imagParts[index])
            return returnVal

        returnVal.real = other.real * self.real
        for indexO in range(len(self.imagParts)):
            for indexI in range(len(other.imagParts)):
                coefficientList = [returnVal.imagParts[q].symbol for q in range(len(returnVal.imagParts))]
                imajCoefficient = self.imagParts[indexO] * other.imagParts[indexI]
                realPart = self.coefficients[indexO] * other.coefficients[indexI]
                if type(imajCoefficient) in [int, float]:
                    returnVal.real+= imajCoefficient * realPart
                    continue

                if imajCoefficient.symbol in coefficientList:
                    algebraIndex = coefficientList.index(imajCoefficient.symbol)
                    returnVal.coefficients[algebraIndex]+= realPart
                    if returnVal.coefficients[algebraIndex] == 0:
                        returnVal.coefficients = returnVal.coefficients[:algebraIndex] + returnVal.coefficients[1+algebraIndex:]
                        returnVal.imagParts = returnVal.imagParts[:algebraIndex] + returnVal.imagParts[1+algebraIndex:]
                    continue
                returnVal.imagParts.append(imajCoefficient)
                returnVal.coefficients.append(realPart)
        for indexO in range(len(other.imagParts)):
            coefficientList = [returnVal.imagParts[q].symbol for q in range(len(returnVal.imagParts))]
            imajCoefficient = other.imagParts[indexO]
            realPart = self.real * other.coefficients[indexO]
            if imajCoefficient.symbol in coefficientList:
                algebraIndex = coefficientList.index(imajCoefficient.symbol)
                returnVal.coefficients[algebraIndex] += realPart
                if returnVal.coefficients[algebraIndex] == 0:
                    returnVal.coefficients = returnVal.coefficients[:algebraIndex] + returnVal.coefficients[1+algebraIndex:]
                    returnVal.imagParts = returnVal.imagParts[:algebraIndex] + returnVal.imagParts[1+algebraIndex:]
                continue
            returnVal.imagParts.append(imajCoefficient)
            returnVal.coefficients.append(realPart)
        for indexO in range(len(self.imagParts)):
            coefficientList = [returnVal.imagParts[q].symbol for q in range(len(returnVal.imagParts))]
            imajCoefficient = self.imagParts[indexO]
            realPart = other.real * self.coefficients[indexO]
            if imajCoefficient.symbol in coefficientList:
                algebraIndex = coefficientList.index(imajCoefficient.symbol)
                returnVal.coefficients[algebraIndex] += realPart
                if returnVal.coefficients[algebraIndex] == 0:
                    returnVal.coefficients = returnVal.coefficients[:algebraIndex] + returnVal.coefficients[1+algebraIndex:]
                    returnVal.imagParts = returnVal.imagParts[:algebraIndex] + returnVal.imagParts[1+algebraIndex:]
                continue
            returnVal.imagParts.append(imajCoefficient)
            returnVal.coefficients.append(realPart)
        return returnVal







ε = imjCoefficient(0, 'ε')
i = imjCoefficient(-1, 'i')
j = imjCoefficient(1, 'j')
h = imjCoefficient(i, 'h')

value = imgObj(2, [h], [3])
otherval = imgObj(2, [h], [-3])

print(f"({value}) * ({otherval}) = {value * otherval}")
