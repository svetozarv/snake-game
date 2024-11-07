from turtle import Screen, Turtle
from time import sleep
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_running = True
while is_running:
    screen.update()
    sleep(0.5)
    snake.move()

    # Check cokkision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Check collisions with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_running = False
        scoreboard.game_over()

    # Detect cokkision wiht tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_running = False
            scoreboard.game_over()

screen.exitonclick()
