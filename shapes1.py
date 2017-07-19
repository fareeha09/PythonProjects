from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
#t.setposition(x_pos, y_pos)

import turtle

def drawCircle(radius, extent, steps):
    counter=0
    turtle.speed(5)
    forward(radius)
    while steps< counter:
        counter+=1


sides= int(input("How many sides do you want your shape to have?"))
### Write your code below:
def draw_shape():
    counter = 0
    while counter <= sides:
        pendown()
        forward(30)
        right(360/sides)
        counter+=1
    penup()

def repeat_shapes():
    answer= int(input("How many times do you want us to repeat your shape?"))
    counter2=0
    while counter2 < answer:
        draw_shape()
        left(360/sides*2)
        counter2+=1
