from turtle import Turtle, Screen
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.title("Pong Game")
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

paddle1 = Turtle()
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)
screen.exitonclick()
