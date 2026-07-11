from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Votre score : {self.score}", align="center", font=("Courier", 24, "normal"))
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal")) 
    def update_score(self):
        self.clear()
        self.write(
            f"Votre score : {self.score}",
            align="center",
            font=("Courier", 24, "normal")
        )

    def increase_score(self):
        self.score += 1
        self.update_score()