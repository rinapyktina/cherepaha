import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.pencolor('#FF1493')
s.bgcolor('black')

t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
for i  in range (1, 210):
    t.forward(i * 3)
    t.right(i)

    t.hideturtle()

turtle.done()
