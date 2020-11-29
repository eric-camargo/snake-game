from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.open_high_score()
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # self.save_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def open_high_score(self):
        with open("score.txt") as file:
            content = file.read()
            self.high_score = int(content)

    def save_high_score(self, score):
        with open("score.txt", "w") as file:
            file.write(str(self.score))