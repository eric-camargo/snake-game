from turtle import Screen
from scoreboard import Scoreboard
import time
import snake
import food

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.title("Snake Game")
my_screen.tracer(0)
my_screen.update()

my_snake =snake.Snake()
my_food = food.Food()
my_score = Scoreboard()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

game_on = True
while game_on:
    my_screen.update()
    time.sleep(my_snake.speed)
    my_snake.move()

    if my_snake.head.distance(my_food) < 10:
        my_food.refresh()
        my_score.add_score()
        my_snake.grow()

    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        game_on = False
        my_score.game_over()

    for segment in my_snake.snake_body[1:]:
        if my_snake.head.distance(segment) < 10:
            game_on = False
            my_score.game_over()


my_screen.exitonclick()
