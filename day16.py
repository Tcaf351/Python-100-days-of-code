# Object Oriented Programming

# Class
# object    # class
# car = CarBlueprint()

# import turtle

# timmy = turtle.Turtle()
from turtle import Turtle, Screen # same as line 7-9
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DeepSkyBlue")

while True:
    timmy.forward(100)
    break

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()