class BigFloat:
    exponent = 0
    mantissa: float

    def __init__(self, num):
        if num is BigFloat:
            self.exponent = num.exponent
            self.mantissa = num.mantissa
            return
        self.mantissa = num
        self.rescale()


    def __str__(self):
        return f"{self.mantissa} x 10^{self.exponent}"

    def rescale(self):
        if self.mantissa == 0:
            self.exponent = 0
            return
        while abs(self.mantissa) >= 10:
            self.exponent+=1
            self.mantissa/=10

        while abs(self.mantissa) < 1:
            self.exponent-=1
            self.mantissa*=10


    def __mul__(self, other):
        if type(other) is not BigFloat:
            newFloat = BigFloat(self.mantissa * other)
            newFloat.exponent+= self.exponent
            newFloat.rescale()
            return newFloat
        newFloat = BigFloat(self.mantissa * other.mantissa)
        newFloat.exponent += self.exponent + other.exponent
        newFloat.rescale()
        return newFloat

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if type(other) is not BigFloat:
            newFloat = BigFloat(self.mantissa / other)
            newFloat.exponent+= self.exponent
            newFloat.rescale()
            return newFloat
        newFloat = BigFloat(self.mantissa / other.mantissa)
        newFloat.exponent += self.exponent - other.exponent
        newFloat.rescale()
        return newFloat


    def __rtruediv__(self, other):
        if type(other) is not BigFloat:
            newFloat = BigFloat(other / self.mantissa)
            newFloat.exponent-= self.exponent
            newFloat.rescale()
            return newFloat
        newFloat = BigFloat(other.mantissa / self.mantissa)
        newFloat.exponent += -self.exponent + other.exponent
        newFloat.rescale()
        return newFloat

    def __add__(self, other):
        if type(other) is not BigFloat:
            return self * BigFloat(other)

        if other.exponent >= self.exponent:
            newFloat = self
            newFloat.exponent = other.exponent
            newFloat.mantissa/= 10 ** (other.exponent - self.exponent)
            newFloat.mantissa+=other.mantissa
            newFloat.rescale()
            return newFloat
        newFloat = other
        newFloat.exponent = self.exponent
        newFloat.mantissa /= 10 ** (self.exponent - other.exponent)
        newFloat.mantissa += self.mantissa
        newFloat.rescale()
        return newFloat

    def __radd__(self, other):
        return other + self


    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other + -self

    def __neg__(self):
        newFloat = BigFloat(-self.mantissa)
        newFloat.exponent += self.exponent
        return newFloat


    def __float__(self):
        return float(self.mantissa * 10 ** self.exponent)

    def __abs__(self):
        return abs(self.mantissa) * 10 ** self.exponent