import turtle as t
import random

COLOR_LIST = ["deep pink", "skyblue", "green", "gold", "orange", "lime", "cyan", "wheat"]
asteroid_list = []


class Asteroid(t.Turtle):
    def __init__(self):
        super().__init__()
        self.create_asteroid()
        self.asteroid_speed = 10

    def create_asteroid(self):
        self.penup()
        self.color(random.choice(COLOR_LIST))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        y_cor = random.randint(-180, 180)
        self.goto(300, y_cor)
        asteroid_list.append(self)

    def move_asteroid(self):
        self.backward(self.asteroid_speed)


