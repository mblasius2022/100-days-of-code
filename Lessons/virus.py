"""
Your module description
"""
import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(10)
t.color('cyan')
t.bgcolor('black')
b = 200
while b > 0:
    t.left(b)
    t.forward(b * 3)
    b = b-1
