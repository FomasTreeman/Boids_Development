import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        if scalar != 0:
            return Vector2D(self.x / scalar, self.y / scalar)
        else:
            pass

    def mag(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def norm(self):
        mag = self.mag()
        if mag == 0:
            return Vector2D(self.x, self.y)
        else:
            return Vector2D(self.x / self.mag(), self.y / self.mag())

    def limit_old(self, limit):
        if self.mag() > limit:
            return self.norm() * limit
        return self

    def limit(self, limit):
        if self.mag() > limit:
            temp = self.norm() * limit
            self.x = temp.x
            self.y = temp.y
