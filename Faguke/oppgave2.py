import turtle


freddy = turtle.Turtle()
freddy.shape("arrow")
freddy.speed(7)

vindu = turtle.Screen()

farge = vindu.textinput("farge", "Fill Colour:  ")
linje = vindu.textinput("linje", "Outside Colour:  ")
sider = int(vindu.numinput("sider", "Hvor mange kanter skall figuren ha: "))
lengde = int(vindu.numinput("lengde", "Hvor stor skal figuren være: "))
vinkel = 360 / sider


def figur():
    freddy.color(linje, farge)
    freddy.begin_fill()
    for i in range(sider - 1):
        freddy.forward(lengde)
        freddy.left(vinkel)
    freddy.end_fill()


def fly():
    freddy.penup()
    freddy.forward(lengde)
    freddy.pendown()


figur()
fly()

vindu.exitonclick()
