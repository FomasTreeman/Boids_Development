from Vector2D import *
import tkinter as tk


class AgentLib:
    def __init__(self, x, y):
        self.position = Vector2D(x, y)
        self.velocity = Vector2D(0, 0)
        self.acceleration = Vector2D(0, 0)
        self.c = None

    def update(self):
        self.velocity += self.acceleration

        self.velocity.limit(5)

        self.position += self.velocity
        self.acceleration *= 0

    def apply_force(self, force):
        self.acceleration += force * 0.1

    def attract(self, other):
        # direction
        force = self.position - other.position
        # force = other.position - self.position
        d = force.mag()
        if d < 5:
            d = 5
        if d > 12:
            d = 12

        force = force.norm()

        # magnitude of force
        strength = (1 * self.mass * other.mass) / (d * d)

        # put it together
        force *= strength

        return force

    def setup(self, window: tk.Canvas):
        window.create_line(self.position.x, self.position.y,
                           self.position.x + self.velocity.x,
                           self.position.y + self.velocity.y, arrow=tk.LAST)
        #self.c = window.create_tex(self.position.x, self.position.y, text="X", anchor=tk.CENTER)

    def display(self, window: tk.Canvas, fill="black"):
        window.coords(self.c, self.position.x, self.position.y)
        window.itemconfig(self.c, fill=fill)

    def edges(self, window: tk.Canvas):
        x = self.position.x
        y = self.position.y
        height = window.winfo_height()
        width = window.winfo_width()
        if x >= width:
            self.position.x = width
            self.velocity.x *= -1
        if x <= 0:
            self.position.x = 0
            self.velocity.x *= -1
        if y >= height:
            self.position.y = height
            self.velocity.y *= -1
        if y <= 0:
            self.position.y = 0
            self.velocity.y *= -1

