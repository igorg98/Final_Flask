import math

class Cube:
    halfLength = 0
    angles = [0, 0, 0]
    vertices = []

    def __init__(self, length):
        self.halfLength = length / 2
        self.vertices = \
        [
            [-self.halfLength, -self.halfLength, -self.halfLength],
            [-self.halfLength, -self.halfLength, self.halfLength],
            [-self.halfLength, self.halfLength, -self.halfLength],
            [-self.halfLength, self.halfLength, self.halfLength],
            [-self.halfLength, -self.halfLength, -self.halfLength],
            [self.halfLength, -self.halfLength, self.halfLength],
            [self.halfLength, self.halfLength, -self.halfLength],
            [self.halfLength, self.halfLength, self.halfLength],
        ]

    def __str__(self):
        Out = ''
        for vert in self.vertices:
            Out += str(vert) + '; '
        return Out

    def Pimp_by_X(self, angle):
        if angle == '':
            return 0
        angle = float(angle)
        cos = float(round(math.cos(math.radians(angle)), 8))
        sin = float(round(math.sin(math.radians(angle)), 8))
        for num in range(8):
            vert = self.vertices[num]
            self.vertices[num] = [vert[0], (cos * vert[1]) - (sin * vert[2]), sin * vert[1] + cos * vert[2]]
        return self

    def Pimp_by_Y(self, angle):
        if angle == '':
            return 0
        angle = float(angle)
        cos = float(round(math.cos(math.radians(angle)), 8))
        sin = float(round(math.sin(math.radians(angle)), 8))
        for num in range(8):
            vert = self.vertices[num]
            self.vertices[num] = [cos * vert[0] - sin * vert[2], vert[1], sin * vert[0] + cos * vert[2]]
        return self

    def Pimp_by_Z(self, angle):
        if angle == '':
            return 0
        angle = float(angle)
        cos = float(round(math.cos(math.radians(angle)), 8))
        sin = float(round(math.sin(math.radians(angle)), 8))
        for num in range(8):
            vert = self.vertices[num]
            self.vertices[num] = [cos * vert[0] - sin * vert[1], sin * vert[0] + cos * vert[1], vert[2]]
        return self