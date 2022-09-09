# Building the snake game part 1 - Animation & Coordinates
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600) # setting the size of the map
screen.bgcolor("black") # setting the background color
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
Scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        Scoreboard.increase_score()
        
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        Scoreboard.game_over()


screen.exitonclick()