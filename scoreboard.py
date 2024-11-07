from turtle import Turtle

FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        # create scoreboard
        self.goto(0, 270)
        self.speed(0)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, "center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()