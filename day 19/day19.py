# Instances, State and Higher Order Functions
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.shape("turtle")

def move_forwards():
    turtle.forward(10)
    
def move_backwards():
    turtle.backward(10)
    
def turn_left():
    turtle.left(10)

def turn_right():
    turtle.right(10)
    
def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen() # listens to the screen
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")


screen.exitonclick()

# Object State and Instances
timmy = Turtle()
tommy = Turtle() # both are instances of the same class

timmy.color("green")
tommy.color("purple") # same instances of the same class but with different attributes