import Vector as V


class Force(V.Vector):
    def __str__(self):
        return f"force of {self.length()}"


def makeForce(vector: V.Vector):
    return Force(vector.x, vector.y)
