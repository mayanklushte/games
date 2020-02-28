from random import randint
from turtle import *

speed(1)
penup()
goto(-100,100)
for step in range(16):
    write(step, align = 'center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()

cac = Turtle()
cac.color('green')
cac.shape('turtle')
cac.penup()
cac.goto(-160,40)
cac.pendown()

dad = Turtle()
dad.color('black')
dad.shape('turtle')
dad.penup()
dad.goto(-160,10)
dad.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  cac.forward(randint(1,5))
  dad.forward(randint(1,5))