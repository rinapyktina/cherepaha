import turtle
wow = turtle.Screen()
wow.bgcolor('black')
waw = turtle.Turtle()
www = turtle.Turtle()

for x in range(1000):
    waw.speed(5000000)
    waw.pencolor('#9370DB')
    waw.left(120)
    waw.forward(x)
    waw.pencolor('#0000FF')
    waw.right(30)
    waw.forward(x)
    www.speed(5000000)
    www.pencolor('#E6E6FA')
    www.left(110)
    www.forward(x)
    www.pencolor('#D8BFD8')
    www.left(110)
    www.forward(x)
