import turtle
import random


main_window = turtle.Screen()
main_window.bgcolor("black")

line = turtle.Turtle()
line.speed(5)
line.penup()
line.goto(-300, 300)
line.color("white")
line.shape("arrow")
for step in range(19):
    line.write(step, align='center')
    line.right(90)
    line.forward(10)
    line.pendown()
    line.forward(300)
    line.penup()
    line.backward(310)
    line.left(90)
    line.forward(20)

# player1
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)
pen.penup()
pen.pencolor("white")
pen.setpos(-300, 30)

# player1
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("turtle")
pen2.pencolor("white")
pen2.penup()
pen2.setpos(-300, 90)

# player1
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.shape("turtle")
pen3.pencolor("white")
pen3.penup()
pen3.setpos(-300, 0)

# player1
pen4 = turtle.Turtle()
pen4.speed(0)
pen4.shape("turtle")
pen4.pencolor("white")
pen4.penup()
pen4.setpos(-300, 120)

for turn in range(115):
    pen.forward(random.randint(1, 5))
    pen2.forward(random.randint(1, 5))
    pen3.forward(random.randint(1, 5))
    pen4.forward(random.randint(1, 5))


