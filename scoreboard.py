import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 215)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Current score: {self.score}", move=False, align="center", font=("ComicSans", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over_man(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("ComicSans", 30, "bold"))
