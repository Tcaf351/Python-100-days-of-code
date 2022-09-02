# Graphical User Interface (GUI)
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.color("red")

timmy_the_turtle.pensize(1)
timmy_the_turtle.pendown()
timmy_the_turtle.forward(10)
timmy_the_turtle.penup()
timmy_the_turtle.forward(10)

screen = Screen()
screen.exitonclick()

# Tuples
tuple = (1, 2, 3) # is similar to a list/array but has rounded brackers and is ordered
# tuples cannot be changed