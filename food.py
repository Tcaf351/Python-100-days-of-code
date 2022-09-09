from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle") # makes the food a circular shape
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5) # size of the circle
        self.color("blue")
        self.speed("fastest") # makes the food appear really fast on the screen
        self.refresh()
        
    
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)