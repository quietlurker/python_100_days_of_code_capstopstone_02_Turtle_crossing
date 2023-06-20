import turtle as t

class SpaceTurtle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.setheading(90)
        self.start_position()

    def move(self):
        self.forward(20)

    def start_position(self):
        self.goto(0, -220)
