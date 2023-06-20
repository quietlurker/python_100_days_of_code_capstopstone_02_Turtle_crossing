import turtle as t
import random

COLOR_LIST = ["deep pink", "skyblue", "green", "gold", "orange", "lime", "cyan", "wheat"]


class Asteroids(t.Turtle):
    def __init__(self):
        super().__init__()
        self.asteroid_list = []
        self.create_asteroid()
        self.asteroid_speed = 10
        self.hideturtle()

    def create_asteroid(self):
        oumuamua = t.Turtle("square")
        oumuamua.penup()
        oumuamua.color(random.choice(COLOR_LIST))
        oumuamua.shape("square")
        oumuamua.shapesize(stretch_wid=1, stretch_len=2)
        y_cor = random.randint(-180, 180)
        oumuamua.goto(300, y_cor)
        self.asteroid_list.append(oumuamua)

    def move_asteroid(self):
        for rock in self.asteroid_list:
            rock.backward(self.asteroid_speed)

    def destroy_asteroids(self):
        for item in self.asteroid_list:
            if item.xcor() < -300:
                item.hideturtle()
                self.asteroid_list.remove(item)

