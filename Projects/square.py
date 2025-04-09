import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("purple")
t.pendown()

t.penup()
t.goto(0, -100)
t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(-100, -100)
t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)

t.penup()
t.goto(-50, -14)
t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)


turtle.exitonclick()